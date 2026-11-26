"""Render one note per node.

Conventions (see SCHEMA.md, "Vault projection"):

* Note path = ``<Folder>/<file-safe name>`` where the name starts with the
  numeric ref for lessons/phases so notes sort in curriculum order.
* Links always use the full path form ``[[Lessons/10-04 Title|10/04 Title]]``.
  Bare ``[[Title]]`` links are ambiguous when two folders hold the same name,
  and ambiguity is exactly what a knowledge graph must not have.
* Frontmatter carries the properties that Bases tables filter on; prose
  attributes go in the body.
* Edge attributes (confidence, note, match tier) are written next to the link
  because a wiki-link cannot carry properties.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from kg import graph_ops
from kg.model import Edge, KnowledgeGraph, Node
from kg.obsidian.preserve import MARKER, Preserved
from kg.paths import Paths

GITHUB_BASE = "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/"
UPSTREAM_PREFIX = "ai-engineering-from-scratch/"

FOLDERS = {
    "phase": "Phases",
    "lesson": "Lessons",
    "track": "Tracks",
    "concept": "Concepts",
    "category": "Categories",
    "artifact": "Artifacts",
    "resource": "Resources",
    "learning_path": "Paths",
    "myth": "Myths",
    "library": "Libraries",
    "community": "Communities",
}

_UNSAFE_RE = re.compile(r'[\\/:*?"<>|#^\[\]]+')


def safe_name(text: str, max_len: int = 110) -> str:
    """File-system and Obsidian-safe note name."""
    text = _UNSAFE_RE.sub("-", text)
    text = re.sub(r"\s+", " ", text).strip(" .-")
    text = re.sub(r"-{2,}", "-", text)
    if len(text) > max_len:
        text = text[:max_len].rstrip(" -")
    return text or "untitled"


# --------------------------------------------------------------------------
# Naming: node -> note path (without .md), unique per folder
# --------------------------------------------------------------------------


@dataclass
class Naming:
    paths: dict[str, str] = field(default_factory=dict)  # node id -> "Folder/Name"
    _used: set[str] = field(default_factory=set)

    def assign(self, node: Node) -> str:
        folder = FOLDERS[node.type]
        base = safe_name(self._base_name(node))
        candidate = f"{folder}/{base}"
        n = 2
        while candidate.lower() in self._used:
            candidate = f"{folder}/{base} ({n})"
            n += 1
        self._used.add(candidate.lower())
        self.paths[node.id] = candidate
        return candidate

    @staticmethod
    def _base_name(node: Node) -> str:
        a = node.attrs
        if node.type == "phase":
            return f"{a['num']:02d} {a['title']}"
        if node.type == "lesson":
            return f"{a['phase']:02d}-{a['num']:02d} {a['title']}"
        if node.type == "track":
            return f"{a['phase']:02d}-{a['letter']} {a.get('title') or ''}".strip()
        if node.type == "artifact":
            return f"{a['lesson'].replace('/', '-')} {a['name']}"
        if node.type == "myth":
            return f"{int(node.id.split(':')[1]):02d} {a['claim']}"
        return node.label

    def has(self, node_id: str) -> bool:
        return node_id in self.paths


# --------------------------------------------------------------------------
# YAML frontmatter (a tiny emitter: strings, ints, bools, flat lists)
# --------------------------------------------------------------------------

_PLAIN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _./()+-]*$")
_RESERVED = {"true", "false", "null", "yes", "no", "on", "off", "~"}


def _yaml_scalar(v: Any) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if _PLAIN_RE.match(s) and s.lower() not in _RESERVED and not re.match(r"^[\d.]+$", s) and not s.endswith(" "):
        return s
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def frontmatter(props: dict[str, Any]) -> str:
    lines = ["---"]
    for k, v in props.items():
        if v is None or v == "" or v == []:
            continue
        if isinstance(v, (list, tuple)):
            lines.append(f"{k}:")
            lines += [f"  - {_yaml_scalar(x)}" for x in v]
        else:
            lines.append(f"{k}: {_yaml_scalar(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Context shared by all renderers
# --------------------------------------------------------------------------


@dataclass
class Ctx:
    g: KnowledgeGraph
    paths: Paths
    naming: Naming
    upstream_linked: bool  # is vault/Upstream a symlink to phases/?
    # Precomputed indexes (built once; renderers are called ~5,000 times)
    out_by: dict[str, list[Edge]] = field(default_factory=lambda: defaultdict(list))
    in_by: dict[str, list[Edge]] = field(default_factory=lambda: defaultdict(list))
    teaches_count: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    cites_count: dict[str, int] = field(default_factory=lambda: defaultdict(int))

    def __post_init__(self) -> None:
        for e in self.g.edges:
            self.out_by[e.src].append(e)
            self.in_by[e.dst].append(e)
            if e.type == "TEACHES":
                self.teaches_count[e.dst] += 1
            if e.type == "CITES" and e.src.startswith("lesson:"):
                self.cites_count[e.dst] += 1

    # ---- links ----
    def short(self, node_id: str) -> str:
        n = self.g.get(node_id)
        if n is None:
            return node_id
        if n.type == "lesson":
            return f"{n.attrs['ref']} {n.attrs['title']}"
        if n.type == "phase":
            return n.label
        return n.label

    def link(self, node_id: str, label: str | None = None) -> str:
        """Wiki-link if the node has a note, plain text otherwise."""
        if self.naming.has(node_id):
            return f"[[{self.naming.paths[node_id]}|{label or self.short(node_id)}]]"
        return label or self.short(node_id)

    def out(self, node_id: str, etype: str) -> list[Edge]:
        return [e for e in self.out_by.get(node_id, []) if e.type == etype]

    def inc(self, node_id: str, etype: str) -> list[Edge]:
        return [e for e in self.in_by.get(node_id, []) if e.type == etype]

    def file_url(self, rel: str | None) -> str | None:
        if not rel:
            return None
        return (self.paths.root / rel).as_uri()

    def github_url(self, rel: str | None) -> str | None:
        if not rel or not rel.startswith(UPSTREAM_PREFIX):
            return None
        return GITHUB_BASE + rel[len(UPSTREAM_PREFIX):]

    def upstream_note_link(self, doc_rel: str | None, label: str = "lesson text in Obsidian") -> str | None:
        """``[[Upstream/10-llms.../04-.../docs/en|label]]`` when the symlink exists."""
        if not self.upstream_linked or not doc_rel:
            return None
        prefix = UPSTREAM_PREFIX + "phases/"
        if not doc_rel.startswith(prefix):
            return None
        inner = doc_rel[len(prefix):]
        if inner.endswith(".md"):
            inner = inner[:-3]
        return f"[[Upstream/{inner}|{label}]]"


def _sort_lessons(ctx: Ctx, ids: Iterable[str]) -> list[str]:
    return sorted(ids, key=lambda i: (ctx.g.get(i).attrs.get("phase", 0), ctx.g.get(i).attrs.get("num", 0)) if ctx.g.get(i) else (99, 0))


def _conf(e: Edge) -> str:
    c = e.attrs.get("confidence")
    return {"high": "", "medium": " ·  medium confidence", "low": " ·  low confidence"}.get(c or "", "")


# --------------------------------------------------------------------------
# Renderers
# --------------------------------------------------------------------------


def render_lesson(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    g = ctx.g
    status_auto = a.get("status") or None
    status = kept.status or status_auto
    tags = [f"phase/{a['phase']:02d}", f"type/{a['lesson_type']}"]
    if status:
        tags.append(f"status/{status}")
    if a.get("on_route"):
        tags.append("route")
    if a.get("community"):
        tags.append(f"community/{a['community']:02d}")
    if a.get("stdlib_only"):
        tags.append("stdlib-only")
    props = {
        "id": n.id, "type": "lesson", "ref": a["ref"], "phase": a["phase"], "num": a["num"],
        "title": a["title"], "lesson_type": a["lesson_type"], "languages": a.get("languages") or [],
        "time_min": a.get("time_min"), "status": status, "status_auto": status_auto,
        "on_route": bool(a.get("on_route")), "route_order": a.get("route_order"),
        "quiz_count": a.get("quiz_count"), "code_files": len(a.get("code_files") or []),
        "concepts": len(ctx.out(n.id, "TEACHES")), "prereqs": len(ctx.out(n.id, "REQUIRES")),
        "community": a.get("community"), "libraries": [g.get(e.dst).attrs["name"] for e in ctx.out(n.id, "USES") if g.get(e.dst)],
        "aliases": [a["ref"], a["ref"].replace("/", "-")], "tags": tags,
        "source": n.source_file, "github": ctx.github_url(a.get("path")),
    }
    lines = [frontmatter(props), f"# {a['ref']} {a['title']}", ""]
    if a.get("hook"):
        lines += [f"> {a['hook']}", ""]

    phase_link = ctx.link(f"phase:{a['phase']}")
    meta = [f"**Phase:** {phase_link}", f"**Type:** {a.get('type_raw') or a['lesson_type']}"]
    if a.get("time_min"):
        meta.append(f"**Time:** {a['time_min']} min")
    if a.get("languages"):
        meta.append("**Languages:** " + ", ".join(a["languages"]))
    meta.append(f"**Status:** {status or '—'}")
    lines.append(" · ".join(meta) + "  ")

    reads = []
    up = ctx.upstream_note_link(a.get("doc_path"))
    if up:
        reads.append(up)
    if ctx.github_url(a.get("path")):
        reads.append(f"[GitHub]({ctx.github_url(a.get('path'))})")
    if a.get("path"):
        reads.append(f"[folder]({ctx.file_url(a['path'])})")
    if a.get("code_files"):
        reads.append(f"code: {', '.join(a['code_files'][:6])}{' …' if len(a['code_files']) > 6 else ''}")
    if a.get("quiz_count"):
        reads.append(f"quiz: {a['quiz_count']} questions")
    lines.append("**Open:** " + " · ".join(reads) + "  ")
    if a.get("evidence"):
        ev = []
        for item in a["evidence"]:
            label, _, rel = item.partition(": ")
            ev.append(f"[{label}]({ctx.file_url(rel)})")
        lines.append("**My work:** " + " · ".join(ev) + "  ")
    for tid_edge in ctx.inc(n.id, "CONTAINS"):
        if tid_edge.src.startswith("track:"):
            lines.append(f"**Track:** {ctx.link(tid_edge.src)}  ")
    comm = ctx.out(n.id, "IN_COMMUNITY")
    uses = ctx.out(n.id, "USES")
    extra = []
    if comm:
        extra.append(f"**Community:** {ctx.link(comm[0].dst)}")
    if uses:
        extra.append("**Libraries:** " + ", ".join(ctx.link(e.dst, g.get(e.dst).attrs["name"]) for e in uses if g.get(e.dst)))
    elif a.get("stdlib_only"):
        extra.append("**Libraries:** standard library only")
    if extra:
        lines.append(" · ".join(extra) + "  ")
    lines.append("")

    # ---- prerequisites ----
    lines += ["## Prerequisites", ""]
    if a.get("prereq_raw"):
        lines += [f"Stated upstream: `{a['prereq_raw']}`", ""]
    reqs = ctx.out(n.id, "REQUIRES")
    grouped: dict[str, list[Edge]] = defaultdict(list)
    singles: list[Edge] = []
    for e in reqs:
        (grouped[e.attrs["group"]] if e.attrs.get("group") else singles).append(e)
    for e in sorted(singles, key=lambda e: e.dst):
        note = f" — {e.attrs['note']}" if e.attrs.get("note") else ""
        via = " ·  from override" if e.attrs.get("via") == "override" else ""
        lines.append(f"- {ctx.link(e.dst)}{note}{_conf(e)}{via}")
    for grp, es in grouped.items():
        es = sorted(es, key=lambda e: e.dst)
        note = f" — {es[0].attrs['note']}" if es[0].attrs.get("note") else ""
        lines.append(f"- **{grp}**{note}{_conf(es[0])}:")
        for e in es:
            lines.append(f"    - {ctx.link(e.dst)}")
    for e in ctx.out(n.id, "REQUIRES_PHASE"):
        note = f" — {e.attrs['note']}" if e.attrs.get("note") else ""
        lines.append(f"- Whole phase: {ctx.link(e.dst)}{note}{_conf(e)}")
    if not reqs and not ctx.out(n.id, "REQUIRES_PHASE"):
        lines.append("- none recorded")
    if a.get("prereq_unparsed"):
        lines.append(f"- Not understood by the parser: {', '.join('`' + u + '`' for u in a['prereq_unparsed'])}")
    lines.append("")

    bridges = ctx.out(n.id, "BRIDGE")
    if bridges:
        lines += ["### Bridges to check first (my plan)", ""]
        for e in bridges:
            note = f" — {e.attrs['note']}" if e.attrs.get("note") else ""
            lines.append(f"- {ctx.link(e.dst)}{note}")
        lines.append("")

    trans = graph_ops.prereqs_of(g, n.id, max_depth=3)
    deeper = {k: d for k, d in trans.items() if d >= 2}
    if deeper:
        lines += ["### Before this lesson (transitive, depth 2–3)", ""]
        by_depth: dict[int, list[str]] = defaultdict(list)
        for k, d in deeper.items():
            by_depth[d].append(k)
        for d in sorted(by_depth):
            lines.append(f"- depth {d}: " + ", ".join(ctx.link(k) for k in _sort_lessons(ctx, by_depth[d])))
        lines.append("")

    deps = [e.src for e in ctx.inc(n.id, "REQUIRES")]
    if deps:
        lines += ["## Builds on this", ""]
        lines += [f"- {ctx.link(d)}" for d in _sort_lessons(ctx, deps)]
        lines.append("")

    # ---- concepts ----
    teaches = ctx.out(n.id, "TEACHES")
    if teaches:
        lines += ["## Concepts taught", ""]
        seen: set[str] = set()
        for e in sorted(teaches, key=lambda e: (e.attrs.get("via") != "key_terms", e.line or 0)):
            if e.dst in seen:
                continue
            seen.add(e.dst)
            c = g.get(e.dst)
            if c is None:
                continue
            kind = "glossary" if c.attrs.get("canonical") else "lesson term"
            definition = e.attrs.get("definition") or c.attrs.get("definition") or ""
            written = e.attrs.get("term_as_written")
            name = ctx.link(e.dst, c.label)
            if written and written.casefold() != c.label.casefold():
                name += f" (as *{written}*)"
            tail = f" — {definition}" if definition else ""
            lines.append(f"- {name} `{kind}`{tail}")
        lines.append("")

    # ---- artifacts ----
    ships = ctx.out(n.id, "SHIPS")
    if ships:
        lines += ["## Ships", ""]
        for e in ships:
            art = g.get(e.dst)
            if art:
                desc = f" — {art.attrs['description']}" if art.attrs.get("description") else ""
                lines.append(f"- {ctx.link(e.dst)} `{art.attrs['kind']}`{desc}")
        lines.append("")

    # ---- further reading ----
    cites = ctx.out(n.id, "CITES")
    if cites:
        lines += ["## Further reading", ""]
        for e in cites:
            r = g.get(e.dst)
            if r is None:
                continue
            others = ctx.cites_count.get(e.dst, 0) - 1
            shared = f" ·  also cited by {others} other lesson{'s' if others != 1 else ''}" if others > 0 else ""
            note = f" — {e.attrs['note']}" if e.attrs.get("note") else ""
            title = ctx.link(e.dst, r.label) if ctx.naming.has(e.dst) else r.label
            lines.append(f"- {title} ([link]({r.attrs['url']})){note}{shared}")
        lines.append("")

    # ---- learning paths ----
    inc = ctx.inc(n.id, "INCLUDES")
    if inc:
        lines += ["## In learning paths", ""]
        for e in inc:
            req = "required" if e.attrs.get("required") else "optional"
            lines.append(f"- {ctx.link(e.src)} — step {e.attrs.get('order')}, {req}")
        lines.append("")

    # ---- route ----
    prev_ = [e.src for e in ctx.inc(n.id, "ROUTE_NEXT")]
    next_ = [e.dst for e in ctx.out(n.id, "ROUTE_NEXT")]
    if a.get("on_route"):
        lines += ["## My route", ""]
        lines.append(f"- Step {a.get('route_order')} in *{a.get('route_section')}*")
        if a.get("route_note"):
            lines.append(f"- Plan note: {a['route_note']}")
        if prev_:
            lines.append(f"- Previous: {ctx.link(prev_[0])}")
        if next_:
            lines.append(f"- Next: {ctx.link(next_[0])}")
        lines.append("")

    lines += ["", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_phase(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    g = ctx.g
    lesson_edges = sorted(ctx.out(n.id, "CONTAINS"), key=lambda e: e.attrs.get("order", 0))
    lessons = [g.get(e.dst) for e in lesson_edges]
    done = sum(1 for l in lessons if l and l.attrs.get("status") == "done")
    props = {
        "id": n.id, "type": "phase", "num": a["num"], "title": a["title"], "hours": a.get("hours"),
        "lessons": len(lessons), "done": done, "aliases": [f"Phase {a['num']}"], "tags": ["phase"],
        "github": ctx.github_url(a.get("path")),
    }
    lines = [frontmatter(props), f"# Phase {a['num']}: {a['title']}", ""]
    meta = [f"**Lessons:** {len(lessons)}"]
    if a.get("hours"):
        meta.append(f"**Estimated:** {a['hours']:g} h")
    meta.append(f"**Done:** {done}")
    if ctx.github_url(a.get("path")):
        meta.append(f"[GitHub]({ctx.github_url(a['path'])})")
    lines += [" · ".join(meta), ""]

    reqs = ctx.out(n.id, "PHASE_REQUIRES")
    unlocks = ctx.inc(n.id, "PHASE_REQUIRES")
    if reqs or unlocks:
        lines += ["## Position in the curriculum", ""]
        if reqs:
            lines.append("- Requires: " + ", ".join(ctx.link(e.dst) for e in reqs))
        if unlocks:
            lines.append("- Unlocks: " + ", ".join(ctx.link(e.src) for e in unlocks))
        lines.append("")

    tracks = [t for t in g.nodes_of_type("track") if t.attrs.get("phase") == a["num"]]
    if tracks:
        lines += ["## Tracks", ""]
        for t in sorted(tracks, key=lambda t: t.attrs["letter"]):
            lines.append(f"- {ctx.link(t.id)} — lessons {t.attrs['start']:02d}–{t.attrs['end']:02d}")
        lines.append("")

    lines += ["## Lessons", "", "| # | Lesson | Type | Time | Status | Concepts |", "|---|---|---|---|---|---|"]
    for l in lessons:
        if l is None:
            continue
        la = l.attrs
        lines.append(
            f"| {la['num']:02d} | {ctx.link(l.id, la['title'])} | {la['lesson_type']} | "
            f"{la.get('time_min') or ''} | {la.get('status') or ''} | {len(ctx.out(l.id, 'TEACHES'))} |"
        )
    lines += ["", "", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_track(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    props = {"id": n.id, "type": "track", "phase": a["phase"], "letter": a["letter"], "title": a.get("title"),
             "tags": ["track", f"phase/{a['phase']:02d}"]}
    lines = [frontmatter(props), f"# Phase {a['phase']} Track {a['letter']}: {a.get('title') or ''}", ""]
    if a.get("note"):
        lines += [f"> {a['note']}", ""]
    lines.append(f"Phase: {ctx.link(f'phase:{a['phase']}')}  ")
    lines += ["", "## Lessons", ""]
    for e in sorted(ctx.out(n.id, "CONTAINS"), key=lambda e: e.attrs.get("order", 0)):
        l = ctx.g.get(e.dst)
        if l:
            lines.append(f"- {ctx.link(e.dst)} — {l.attrs.get('status') or ''}")
    users = sorted({e.src for e in ctx.g.edges if e.type == "REQUIRES" and e.attrs.get("group") == f"Track {a['letter']}"})
    if users:
        lines += ["", "## Required (as a whole) by", ""] + [f"- {ctx.link(u)}" for u in _sort_lessons(ctx, users)]
    lines += ["", "", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_concept(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    g = ctx.g
    canonical = bool(a.get("canonical"))
    taught = graph_ops.concept_lessons(g, n.id)
    cat_edge = ctx.out(n.id, "IN_CATEGORY")
    tags = ["concept/glossary" if canonical else "concept/lesson-term"]
    if cat_edge:
        c = g.get(cat_edge[0].dst)
        if c:
            tags.append("category/" + cat_edge[0].dst.split(":", 1)[1])
    if a.get("community"):
        tags.append(f"community/{a['community']:02d}")
    props = {
        "id": n.id, "type": "concept", "name": a.get("name"), "canonical": canonical,
        "category": a.get("category"), "aliases": a.get("aliases") or [], "taught_in": len(taught),
        "community": a.get("community"), "tags": tags, "source": n.source_file,
    }
    lines = [frontmatter(props), f"# {n.label}", ""]
    comm = ctx.out(n.id, "IN_COMMUNITY")
    if comm:
        lines += [f"**Community:** {ctx.link(comm[0].dst)}", ""]
    if a.get("folk_definition"):
        lines += [f"> *What people say:* {a['folk_definition']}", ""]
    if a.get("definition"):
        lines += [f"**What it actually means:** {a['definition']}", ""]
    for key, title in (("why_it_matters", "Why it matters"), ("in_practice", "In practice"),
                       ("confusion", "Common confusion"), ("etymology", "Why it's called that")):
        if a.get(key):
            lines += [f"**{title}:** {a[key]}", ""]
    if cat_edge:
        lines += [f"**Category:** {ctx.link(cat_edge[0].dst)}", ""]
    if not canonical:
        lines += ["*Not in the glossary: this concept exists because lessons list it in their Key Terms table. "
                  "If it is really a glossary term under another name, add it to `data/aliases.json`.*", ""]

    rel = ctx.out(n.id, "RELATED_TO") + ctx.inc(n.id, "RELATED_TO")
    if rel:
        ids = sorted({e.dst if e.src == n.id else e.src for e in rel})
        lines += ["## Related concepts", ""] + [f"- {ctx.link(i)}" for i in ids] + [""]

    if taught:
        lines += ["## Taught in", ""]
        # local definition per lesson, when the lesson's Key Terms row differs
        for lid, tier in sorted(taught, key=lambda t: t[0]):
            e = next((e for e in ctx.inc(n.id, "TEACHES") if e.src == lid and e.attrs.get("via") == "key_terms"), None)
            local = e.attrs.get("definition") if e else ""
            tail = f" — {local}" if local and local != a.get("definition") else ""
            tier_txt = "" if tier in ("exact", "new") else f" `{tier}`"
            lines.append(f"- {ctx.link(lid)}{tier_txt}{tail}")
        lines.append("")

    cites = ctx.out(n.id, "CITES")
    if cites:
        lines += ["## Sources", ""]
        for e in cites:
            r = g.get(e.dst)
            if r:
                lines.append(f"- {ctx.link(e.dst, r.label) if ctx.naming.has(e.dst) else r.label} ([link]({r.attrs['url']}))")
        lines.append("")
    lines += ["", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_category(ctx: Ctx, n: Node, kept: Preserved) -> str:
    members = sorted((e.src for e in ctx.inc(n.id, "IN_CATEGORY")), key=lambda i: ctx.g.get(i).label if ctx.g.get(i) else i)
    props = {"id": n.id, "type": "category", "name": n.attrs.get("name"), "concepts": len(members), "tags": ["category"]}
    lines = [frontmatter(props), f"# {n.label}", "", f"{len(members)} glossary concepts.", "", "## Concepts", ""]
    lines += [f"- {ctx.link(i)}" for i in members]
    lines += ["", "", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_artifact(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    owner = [e.src for e in ctx.inc(n.id, "SHIPS")]
    props = {"id": n.id, "type": "artifact", "name": a["name"], "kind": a["kind"], "version": a.get("version"),
             "lesson": a.get("lesson"), "tags": [f"artifact/{a['kind']}"] + [f"topic/{t}" for t in a.get("tags") or []],
             "source": n.source_file}
    lines = [frontmatter(props), f"# {a['name']}", ""]
    if a.get("description"):
        lines += [f"> {a['description']}", ""]
    meta = [f"**Kind:** {a['kind']}" + (" (bundle)" if a.get("bundle") else "")]
    if a.get("version"):
        meta.append(f"**Version:** {a['version']}")
    if owner:
        meta.append(f"**From:** {ctx.link(owner[0])}")
    if a.get("path"):
        meta.append(f"[open file]({ctx.file_url(a['path'])})")
        if ctx.github_url(a["path"]):
            meta.append(f"[GitHub]({ctx.github_url(a['path'])})")
    lines += [" · ".join(meta), "", "", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_resource(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    cited_l = [e for e in ctx.inc(n.id, "CITES") if e.src.startswith("lesson:")]
    cited_c = [e for e in ctx.inc(n.id, "CITES") if e.src.startswith("concept:")]
    props = {"id": n.id, "type": "resource", "title": a["title"], "url": a["url"], "kind": a["kind"], "host": a.get("host"),
             "cited_by": len(cited_l), "tags": [f"resource/{a['kind']}"]}
    lines = [frontmatter(props), f"# {n.label}", "", f"[{a['url']}]({a['url']})", ""]
    if cited_l:
        lines += ["## Cited by lessons", ""]
        for e in sorted(cited_l, key=lambda e: e.src):
            note = f" — {e.attrs['note']}" if e.attrs.get("note") else ""
            lines.append(f"- {ctx.link(e.src)}{note}")
        lines.append("")
    if cited_c:
        lines += ["## Cited by glossary concepts", ""] + [f"- {ctx.link(e.src)}" for e in cited_c] + [""]
    lines += ["", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_learning_path(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    steps = sorted(ctx.out(n.id, "INCLUDES"), key=lambda e: (not e.attrs.get("required"), e.attrs.get("order") or 0))
    props = {"id": n.id, "type": "learning_path", "title": a.get("title"), "kind": a.get("kind"), "minutes": a.get("minutes"),
             "steps": len(steps), "tags": ["path"], "source": n.source_file}
    lines = [frontmatter(props), f"# {n.label}", ""]
    if a.get("summary"):
        lines += [f"> {a['summary']}", ""]
    if a.get("minutes"):
        lines += [f"**Estimated:** {a['minutes']} min", ""]
    lines += ["## Steps", "", "| # | Lesson | Required | Min | Status |", "|---|---|---|---|---|"]
    for e in steps:
        l = ctx.g.get(e.dst)
        if l:
            lines.append(f"| {e.attrs.get('order') or ''} | {ctx.link(e.dst)} | {'yes' if e.attrs.get('required') else 'optional'} | "
                         f"{e.attrs.get('minutes') or ''} | {l.attrs.get('status') or ''} |")
    lines += ["", "", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_myth(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    props = {"id": n.id, "type": "myth", "claim": a["claim"], "tags": ["myth"], "source": n.source_file}
    lines = [frontmatter(props), f"# Myth: “{a['claim']}”", ""]
    if a.get("reality"):
        lines += [f"**Reality:** {a['reality']}", ""]
    if a.get("why_it_matters"):
        lines += [f"**Why it matters:** {a['why_it_matters']}", ""]
    lines += ["", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_library(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    users = sorted(ctx.inc(n.id, "USES"), key=lambda e: e.src)
    props = {"id": n.id, "type": "library", "name": a["name"], "language": a["language"], "used_by": len(users),
             "tags": ["library", f"lang/{a['language']}"]}
    lines = [frontmatter(props), f"# {n.label}", "", f"Imported as `{a['import_name']}` in {len(users)} lessons.", "",
             "## Used in", ""]
    for e in users:
        files = ", ".join(e.attrs.get("files", [])[:3])
        lines.append(f"- {ctx.link(e.src)} — {files}")
    lines += ["", "", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


def render_community(ctx: Ctx, n: Node, kept: Preserved) -> str:
    a = n.attrs
    g = ctx.g
    members = [e.src for e in ctx.inc(n.id, "IN_COMMUNITY")]
    lessons = _sort_lessons(ctx, [m for m in members if m.startswith("lesson:")])
    concepts = sorted((m for m in members if m.startswith("concept:")), key=lambda m: g.get(m).label if g.get(m) else m)
    props = {"id": n.id, "type": "community", "num": a["num"], "name": a["name"], "lessons": a["lessons"],
             "concepts": a["concepts"], "phases": [str(p) for p in a.get("phases") or []], "tags": ["community"]}
    lines = [frontmatter(props), f"# Community {a['num']:02d}: {a['name']}", "",
             "A cluster found by label propagation over TEACHES, REQUIRES, BRIDGE and RELATED_TO edges "
             "(see `kg/communities.py`). The name is the three most connected concepts inside it, no LLM involved.", ""]
    if a.get("phases"):
        lines += ["**Phases:** " + ", ".join(ctx.link(f"phase:{p}", f"Phase {p}") for p in a["phases"]), ""]
    if lessons:
        lines += ["## Lessons", ""] + [f"- {ctx.link(l)} — {g.get(l).attrs.get('status') or ''}" for l in lessons] + [""]
    if concepts:
        lines += ["## Concepts", ""]
        for c in concepts:
            cn = g.get(c)
            kind = "glossary" if cn and cn.attrs.get("canonical") else "lesson term"
            lines.append(f"- {ctx.link(c)} `{kind}`")
        lines.append("")
    lines += ["", MARKER, "", kept.notes]
    return "\n".join(lines).rstrip() + "\n"


RENDERERS = {
    "library": render_library,
    "community": render_community,
    "phase": render_phase,
    "lesson": render_lesson,
    "track": render_track,
    "concept": render_concept,
    "category": render_category,
    "artifact": render_artifact,
    "resource": render_resource,
    "learning_path": render_learning_path,
    "myth": render_myth,
}


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------


def render_home(ctx: Ctx, exported: dict[str, int]) -> str:
    g = ctx.g
    lines = [frontmatter({"type": "home", "tags": ["home"], "built": g.meta.get("built_at"), "upstream_commit": g.meta.get("upstream_commit")}),
             "# AI Engineering from Scratch — knowledge graph", ""]
    lines += ["Generated from `build/graph.json`. Rebuild with `uv run python -m kg.cli all`. "
              "Everything above the *my notes* marker in a generated note is overwritten; everything below it, "
              "and everything in `My Notes/`, is yours.", ""]
    lines += ["## Tables", "", "- [[Bases/Lessons.base|All lessons]] · [[Bases/My Route.base|My route]] · "
              "[[Bases/Concepts.base|Concepts]] · [[Bases/Resources.base|Resources]] · [[Bases/Artifacts.base|Artifacts]] · "
              "[[Bases/Libraries.base|Libraries]] · [[Bases/Communities.base|Communities]]", ""]

    route = sorted((n for n in g.nodes_of_type("lesson") if n.attrs.get("on_route")), key=lambda n: n.attrs.get("route_order") or 0)
    if route:
        lines += ["## My route", "", "| Step | Lesson | Status | Bridges |", "|---|---|---|---|"]
        for n in route:
            bridges = ", ".join(ctx.link(e.dst, ctx.g.get(e.dst).attrs["ref"]) for e in ctx.out(n.id, "BRIDGE") if ctx.g.get(e.dst))
            lines.append(f"| {n.attrs.get('route_order')} | {ctx.link(n.id)} | {n.attrs.get('status') or ''} | {bridges} |")
        lines.append("")

    lines += ["## Phases", "", "| # | Phase | Lessons | Done | Hours | Requires |", "|---|---|---|---|---|---|"]
    for p in sorted(g.nodes_of_type("phase"), key=lambda p: p.attrs["num"]):
        lessons = [g.get(e.dst) for e in ctx.out(p.id, "CONTAINS")]
        done = sum(1 for l in lessons if l and l.attrs.get("status") == "done")
        req = ", ".join(ctx.link(e.dst, f"P{g.get(e.dst).attrs['num']}") for e in ctx.out(p.id, "PHASE_REQUIRES") if g.get(e.dst))
        lines.append(f"| {p.attrs['num']} | {ctx.link(p.id, p.attrs['title'])} | {len(lessons)} | {done} | {p.attrs.get('hours') or ''} | {req} |")
    lines.append("")

    comms = sorted(g.nodes_of_type("community"), key=lambda c: c.attrs["num"])
    if comms:
        lines += ["## Communities (what the data clusters, across phases)", "", "| # | Cluster | Lessons | Concepts | Phases |", "|---|---|---|---|---|"]
        for c in comms[:30]:
            lines.append(f"| {c.attrs['num']} | {ctx.link(c.id, c.attrs['name'])} | {c.attrs['lessons']} | {c.attrs['concepts']} | "
                         f"{', '.join(str(p) for p in c.attrs.get('phases') or [])} |")
        if len(comms) > 30:
            lines.append(f"| … | {len(comms) - 30} smaller clusters in `Communities/` | | | |")
        lines.append("")

    libs = sorted(g.nodes_of_type("library"), key=lambda l: -len(ctx.inc(l.id, "USES")))
    if libs:
        lines += ["## Libraries", ""] + [f"- {ctx.link(l.id)} — {len(ctx.inc(l.id, 'USES'))} lessons" for l in libs[:15]] + [""]

    lines += ["## Learning paths", ""] + [f"- {ctx.link(p.id)}" for p in sorted(g.nodes_of_type("learning_path"), key=lambda p: p.label)] + [""]
    lines += ["## Glossary categories", ""] + [f"- {ctx.link(c.id)} ({len(ctx.inc(c.id, 'IN_CATEGORY'))})" for c in sorted(g.nodes_of_type("category"), key=lambda c: c.label)] + [""]
    lines += ["## Myths", ""] + [f"- {ctx.link(m.id)}" for m in sorted(g.nodes_of_type("myth"), key=lambda m: int(m.id.split(':')[1]))] + [""]

    lines += ["## What is in this vault", "", "| Folder | Notes |", "|---|---|"]
    for folder, count in sorted(exported.items()):
        lines.append(f"| {folder} | {count} |")
    lines += ["", "Graph counts (all of them, including nodes without a note): "
              + ", ".join(f"{k} {v}" for k, v in g.node_counts().items()), ""]
    return "\n".join(lines).rstrip() + "\n"
