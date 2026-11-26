"""The quality report: what the build found, and what it could not place.

Why this module exists
----------------------
A knowledge graph built by parsers is only as good as the parts you can *see*
failing. This report is the habit that keeps the graph honest: after every
build you read it, and every number here is a question ("why are 12 lessons
without prerequisites edges?") before it becomes a fact in the vault.

Sections
--------
1. Counts per node and edge type (sanity: 20 phases, 523 lessons, ...).
2. Validation problems from ``KnowledgeGraph.validate`` (should be empty).
3. Extractor problems (missing lessons referenced, unknown tracks, ...).
4. Unparsed prerequisite fragments, grouped by text, with the lessons that
   contain them: the to-do list for ``data/prereq_overrides.json``.
5. Key Terms matching statistics and the most frequent unmatched terms:
   the to-do list for ``data/aliases.json``.
6. Resources cited by more than one lesson (proof that canonicalisation works).
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Any

from kg.model import KnowledgeGraph


@dataclass
class BuildStats:
    """Everything the extractors report back, collected by ``kg.build``."""

    problems: dict[str, list[str]] = field(default_factory=dict)  # stage -> problems
    key_terms: Any = None  # KeyTermStats
    validation: list[str] = field(default_factory=list)
    upstream_commit: str | None = None
    built_at: str | None = None


def _md_table(header: list[str], rows: list[list[Any]]) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)


def render_report(g: KnowledgeGraph, stats: BuildStats) -> str:
    out: list[str] = ["# Build report", ""]
    out.append(f"Built at: {stats.built_at}  ")
    out.append(f"Upstream commit: `{stats.upstream_commit}`  ")
    out.append("")

    # 1. counts
    out += ["## Counts", ""]
    out.append(_md_table(["Node type", "Count"], [[k, v] for k, v in g.node_counts().items()]))
    out.append("")
    out.append(_md_table(["Edge type", "Count"], [[k, v] for k, v in g.edge_counts().items()]))
    out.append("")

    lessons = g.nodes_of_type("lesson")
    with_prereq_edges = {e.src for e in g.edges if e.type in ("REQUIRES", "REQUIRES_PHASE")}
    no_prereq_field = [n for n in lessons if not n.attrs.get("prereq_raw")]
    none_field = [n for n in lessons if (n.attrs.get("prereq_raw") or "").strip().lower().rstrip(".") == "none"]
    unresolved = [n for n in lessons if n.attrs.get("prereq_raw") and n.id not in with_prereq_edges and n not in none_field]
    out += ["### Lesson coverage", ""]
    out.append(_md_table(["Metric", "Value"], [
        ["lessons", len(lessons)],
        ["lessons with at least one prerequisite edge", len(with_prereq_edges)],
        ["lessons whose field says None", len(none_field)],
        ["lessons without a Prerequisites field", len(no_prereq_field)],
        ["lessons with a field but zero edges (parser miss)", len(unresolved)],
        ["lessons with TEACHES edges", len({e.src for e in g.edges if e.type == 'TEACHES'})],
        ["lessons with CITES edges", len({e.src for e in g.edges if e.type == 'CITES' and e.src.startswith('lesson:')})],
        ["lessons with SHIPS edges", len({e.src for e in g.edges if e.type == 'SHIPS'})],
    ]))
    out.append("")
    if unresolved:
        out.append("Lessons with a Prerequisites field but no edge:")
        out.append("")
        for n in sorted(unresolved, key=lambda n: n.id):
            out.append(f"- `{n.attrs['ref']}` {n.attrs['title']}: `{n.attrs['prereq_raw']}`")
        out.append("")

    # 2. validation
    out += ["## Validation", ""]
    if stats.validation:
        out += [f"- {p}" for p in stats.validation]
    else:
        out.append("No dangling edges, no type mismatches, no self-loops.")
    out.append("")

    # 3. extractor problems
    out += ["## Extractor problems", ""]
    total = sum(len(v) for v in stats.problems.values())
    if total == 0:
        out.append("None.")
    for stage, probs in stats.problems.items():
        if not probs:
            continue
        out.append(f"### {stage} ({len(probs)})")
        out.append("")
        out += [f"- {p}" for p in probs[:200]]
        if len(probs) > 200:
            out.append(f"- ... {len(probs) - 200} more")
        out.append("")

    # 4. unparsed prerequisite fragments
    frags: dict[str, list[str]] = defaultdict(list)
    for n in lessons:
        for f in n.attrs.get("prereq_unparsed") or []:
            frags[f].append(n.attrs["ref"])
    out += [f"## Unparsed prerequisite fragments ({sum(len(v) for v in frags.values())} in {len(frags)} distinct)", ""]
    if not frags:
        out.append("None.")
    for f, refs in sorted(frags.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        out.append(f"- `{f}` — {', '.join(refs[:8])}{' ...' if len(refs) > 8 else ''}")
    out.append("")

    # 5. key terms
    kt = stats.key_terms
    if kt is not None:
        out += ["## Key Terms matching", ""]
        matched = kt.rows - kt.by_tier.get("new", 0)
        rate = (matched / kt.rows * 100) if kt.rows else 0
        out.append(_md_table(["Metric", "Value"], [
            ["lessons with a Key Terms table", kt.lessons_with_table],
            ["rows", kt.rows],
            ["matched to a glossary term", f"{matched} ({rate:.1f}%)"],
            ["  exact", kt.by_tier.get("exact", 0)],
            ["  alias", kt.by_tier.get("alias", 0)],
            ["  normalized", kt.by_tier.get("normalized", 0)],
            ["new (non-canonical) concepts created", kt.by_tier.get("new", 0)],
            ["distinct non-canonical concepts", len(kt.unmatched)],
        ]))
        out.append("")
        out.append("Most frequent unmatched terms (candidates for `data/aliases.json`):")
        out.append("")
        for term, count in kt.unmatched.most_common(40):
            out.append(f"- {term} ({count})")
        out.append("")

    # 6. shared resources
    cites: Counter = Counter(e.dst for e in g.edges if e.type == "CITES" and e.src.startswith("lesson:"))
    shared = [(rid, c) for rid, c in cites.most_common() if c >= 2]
    out += [f"## Resources cited by 2+ lessons ({len(shared)})", ""]
    for rid, c in shared[:30]:
        node = g.get(rid)
        out.append(f"- {node.label if node else rid} — {c} lessons")
    out.append("")

    # 7. concept hubs
    teaches: Counter = Counter(e.dst for e in g.edges if e.type == "TEACHES")
    out += ["## Concepts taught by the most lessons", ""]
    for cid, c in teaches.most_common(25):
        node = g.get(cid)
        flag = "" if node and node.attrs.get("canonical") else " (non-canonical)"
        out.append(f"- {node.label if node else cid}{flag} — {c} lessons")
    out.append("")

    # 8. libraries
    uses: Counter = Counter(e.dst for e in g.edges if e.type == "USES")
    out += ["## Libraries used by the most lessons", ""]
    for lid, c in uses.most_common(20):
        node = g.get(lid)
        out.append(f"- {node.label if node else lid} — {c} lessons")
    stdlib_only = sum(1 for n in lessons if n.attrs.get("stdlib_only"))
    out += ["", f"Python lessons that need nothing outside the standard library: {stdlib_only}", ""]

    # 9. communities
    comms = sorted(g.nodes_of_type("community"), key=lambda n: n.attrs["num"])
    out += [f"## Communities ({len(comms)} with at least 4 members)", ""]
    if comms:
        out.append(_md_table(["#", "Label", "Lessons", "Concepts", "Phases"], [
            [c.attrs["num"], c.attrs["name"], c.attrs["lessons"], c.attrs["concepts"],
             ", ".join(str(p) for p in c.attrs["phases"])] for c in comms[:40]]))
    unassigned = sum(1 for n in lessons if not n.attrs.get("community"))
    out += ["", f"Lessons in no community (isolated or in a cluster smaller than 4): {unassigned}", ""]
    return "\n".join(out)
