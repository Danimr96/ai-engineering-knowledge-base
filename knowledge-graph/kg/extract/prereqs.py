"""Turn the free-text ``**Prerequisites:**`` field into REQUIRES edges.

Why this is the hardest extractor
---------------------------------
The field is written by hand in at least a dozen shapes::

    Phase 7 · 02 (Self-Attention from Scratch)
    Phase 1, Lessons 01-04
    Phase 11 Lesson 01 (Prompt Engineering), Lesson 09 (Function Calling)
    Lesson 03.02 (Multi-Layer Networks)
    Lessons 30 through 32 of this phase
    Phase 6 · 04, 06, 07, 09, 10; Phase 2 · 09 (Model Evaluation)
    Phases 14 · 32 to 14 · 40
    Phase 19 Track B foundations, lessons 70 and 71
    all of Phase 16 (Lessons 01-24)
    Phase 1 · Calculus
    None

A ``split(",")`` cannot work: the comma separates items, joins "Phase 1, Lesson
06", lists numbers, and appears inside parentheses. So this module is a small
**scanner with state**: it walks the string left to right, matches the most
specific pattern available at the current position, and remembers the last
phase mentioned ("sticky phase") so that a bare "Lesson 09" knows which phase
it belongs to.

Two-step design
---------------
1. ``parse_prereq_text`` is a *pure function*: text in, list of ``Ref`` out.
   No filesystem, no graph. That is what makes it testable with a table of
   forty real strings.
2. ``resolve`` turns refs into edges against the lessons that actually exist,
   expanding ranges, collapsing whole-phase ranges to REQUIRES_PHASE, and
   reporting everything it could not place.

Every edge keeps the raw text (``raw``) and the exact fragment (``span``) so a
wrong edge in the vault can be traced to the words that produced it.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from kg.model import Edge, KnowledgeGraph, lesson_id, phase_id
from kg.paths import Paths

# --------------------------------------------------------------------------
# Data
# --------------------------------------------------------------------------


@dataclass
class Ref:
    """One reference found in the text.

    kind: 'lesson' (one lesson), 'range' (start..end in one phase),
          'phase' (a whole phase), 'track' (a Phase 19 track letter)
    """

    kind: str
    phase: int | None
    start: int | None = None
    end: int | None = None
    letter: str | None = None
    raw: str = ""
    note: str = ""
    mention: int = -1  # index of the phase mention this ref hangs from
    has_items: bool = False  # for 'phase' refs: did explicit lessons follow?
    adjacent_list: bool = False  # for 'track' refs: did a lesson list follow directly?


@dataclass
class ParseResult:
    refs: list[Ref] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    unparsed: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------
# Patterns. Order of attempts in the scanner: most specific first.
# --------------------------------------------------------------------------

_RANGE_SEP = r"\s*(?:-|–|—|to|through)\s*"
_NUM = r"(?<!\d)(\d{1,2})(?!\d)"

# "Phases 14 · 32 to 14 · 40"  /  "Phase 14 · 32 to 40"
RE_PHASES_MIDDOT_RANGE = re.compile(
    r"Phases?\s+(?<!\d)(\d{1,2})\s*·\s*(\d{1,2})" + _RANGE_SEP + r"(?:(\d{1,2})\s*·\s*)?(\d{1,2})(?!\d)"
)
# "Phase 7", "Phases 14", "all of Phase 16", "All Phase 10"
RE_PHASE = re.compile(r"(?:[Aa]ll\s+(?:of\s+)?)?Phases?\s+(?<!\d)(\d{1,2})(?!\d)(?!\.\d)")
# " · " followed by a number: the mid-dot lesson list form
RE_MIDDOT = re.compile(r"\s*·\s*(?=\d)")
# "Lesson 09", "Lessons 01-04", "lessons 70 and 71"
RE_LESSON_KW = re.compile(r"[Ll]essons?\s+(?=\d)")
# One list item: "09", "03.02" (phase.lesson), "01-04", "30 through 32"
RE_ITEM = re.compile(r"(?<!\d)(\d{1,2})(?:\.(\d{2}))?(?:" + _RANGE_SEP + r"(\d{1,2}))?(?![\d.])")
# Separator that continues a list only when a number follows
RE_CONT = re.compile(r"\s*(?:,\s*(?:and\s+)?|;\s*|\s+and\s+)(?=\d{1,2}(?!\d))")
# Title words after an item ("09 Information Theory, 06 ...") – no digits/commas
RE_TITLE_WORDS = re.compile(r"\s+(?=[A-Za-z])[^,;()\d·]*")
RE_TRACK = re.compile(r"Track\s+([A-E])(\d)?\b")
RE_PAREN = re.compile(r"\(([^()]*)\)")
RE_THIS_PHASE = re.compile(r"\bthis phase\b", re.IGNORECASE)
RE_SEP = re.compile(r"[,;.:]+|\band\b|·")
# A word never swallows a separator, so "lessons," becomes "lessons" + ","
RE_WORD = re.compile(r"[^\s,;.:·]+")

# Parenthetical content that is really a lesson list, not a title
RE_PAREN_HAS_LESSONS = re.compile(r"[Ll]essons?\s+\d")
RE_PAREN_NUMBER_LIST = re.compile(r"^\s*\d{1,2}(?:\s*(?:,\s*(?:and\s+)?|\s+and\s+)\d{1,2})*\s*$")
RE_PAREN_RANGE = re.compile(r"^\s*\d{1,2}" + _RANGE_SEP + r"\d{1,2}\s*$")

# Words that are filler, not a missed reference
RE_IGNORABLE = re.compile(
    r"^(?:(?:all|of|this|phase|lessons?|foundations?|transformer|safety|prior|covering|engines|track|and|the|"
    r"especially|referenced)\s*)+$",
    re.IGNORECASE,
)


# --------------------------------------------------------------------------
# Scanner
# --------------------------------------------------------------------------


class _Scanner:
    """Walks one prerequisite string. See module docstring for the grammar."""

    def __init__(self, text: str, current_phase: int) -> None:
        self.text = text
        self.pos = 0
        self.current_phase = current_phase  # phase of the lesson being parsed
        self.sticky_phase: int | None = None  # last phase explicitly mentioned
        self.result = ParseResult()
        self.last_ref: Ref | None = None
        self.mentions: list[Ref] = []
        self.last_track: Ref | None = None
        self.last_track_end = -1
        self.residue: list[str] = []

    # ---- helpers ------------------------------------------------------
    def _flush_residue(self) -> None:
        if not self.residue:
            return
        fragment = " ".join(self.residue).strip()
        self.residue = []
        if not fragment:
            return
        if RE_IGNORABLE.match(fragment):
            return
        self.result.unparsed.append(fragment)

    def _add(self, ref: Ref) -> Ref:
        self._flush_residue()
        self.result.refs.append(ref)
        self.last_ref = ref
        return ref

    def _mention(self, phase: int, raw: str) -> Ref:
        ref = Ref(kind="phase", phase=phase, raw=raw, mention=len(self.mentions))
        self.mentions.append(ref)
        self.sticky_phase = phase
        self._add(ref)
        return ref

    def _attach(self, ref: Ref, list_start: int) -> None:
        """Hang a lesson/range ref from the current phase mention, if it matches."""
        if self.mentions and ref.phase == self.mentions[-1].phase:
            self.mentions[-1].has_items = True
            ref.mention = self.mentions[-1].mention
        # A lesson list right after "Track X" (no comma between) *defines* the
        # track ("Track C lessons 42-49"); the explicit numbers win.
        if self.last_track is not None and self.last_track_end >= 0:
            between = self.text[self.last_track_end : list_start]
            if not re.search(r"[,;]", between):
                self.last_track.adjacent_list = True

    # ---- items --------------------------------------------------------
    def _parse_items(self, phase_hint: int | None) -> None:
        """Parse ``N``, ``N-M``, ``P.NN`` items joined by commas/and/semicolons.

        The whole list is collected first and only then attached, because a
        trailing "of this phase" ("Lessons 30 and 31 of this phase") changes
        the phase of *every* item in the list, not just the last one.
        """
        items: list[Ref] = []
        list_start: int | None = None
        this_phase = False
        while True:
            m = RE_ITEM.match(self.text, self.pos)
            if not m:
                break
            if list_start is None:
                list_start = m.start()
            self.pos = m.end()
            a, dotted, b = m.group(1), m.group(2), m.group(3)
            if dotted is not None:  # "03.02" -> phase 3, lesson 2
                ref = Ref(kind="lesson", phase=int(a), start=int(dotted), raw=m.group(0))
            else:
                phase = phase_hint if phase_hint is not None else self.current_phase
                if b is not None:
                    ref = Ref(kind="range", phase=phase, start=int(a), end=int(b), raw=m.group(0))
                else:
                    ref = Ref(kind="lesson", phase=phase, start=int(a), raw=m.group(0))
            items.append(ref)
            # optional "(title)" right after the number
            pm = RE_PAREN.match(self.text, self._skip_ws(self.pos))
            if pm and not self._paren_is_list(pm.group(1)):
                ref.note = pm.group(1).strip()
                self.pos = pm.end()
            # optional title words: "09 Information Theory, 06 Probability"
            tm = RE_TITLE_WORDS.match(self.text, self.pos)
            if tm and RE_CONT.match(self.text, tm.end()):
                self._absorb_words(ref, tm.group(0))
                self.pos = tm.end()
                this_phase = this_phase or bool(RE_THIS_PHASE.search(tm.group(0)))
            cm = RE_CONT.match(self.text, self.pos)
            if not cm:
                # List is over. Trailing words ("... 18 Convex Optimization",
                # "... 31 of this phase") describe the last item.
                if tm:
                    self._absorb_words(ref, tm.group(0))
                    self.pos = tm.end()
                    this_phase = this_phase or bool(RE_THIS_PHASE.search(tm.group(0)))
                break
            self.pos = cm.end()
        if this_phase:
            for ref in items:
                if ref.raw and "." not in ref.raw:
                    ref.phase = self.current_phase
        for ref in items:
            self._add(ref)
            self._attach(ref, list_start if list_start is not None else self.pos)

    @staticmethod
    def _absorb_words(ref: Ref, words: str) -> None:
        note = re.sub(r"\bof this phase\b|\bthis phase\b", "", words, flags=re.IGNORECASE).strip(" ,;-")
        if note and not ref.note and not RE_IGNORABLE.match(note):
            ref.note = note

    def _skip_ws(self, pos: int) -> int:
        while pos < len(self.text) and self.text[pos] == " ":
            pos += 1
        return pos

    @staticmethod
    def _paren_is_list(content: str) -> bool:
        return bool(
            RE_PAREN_HAS_LESSONS.search(content)
            or RE_PAREN_NUMBER_LIST.match(content)
            or RE_PAREN_RANGE.match(content)
        )

    # ---- main loop ----------------------------------------------------
    def run(self) -> ParseResult:
        text = self.text
        n = len(text)
        while self.pos < n:
            if text[self.pos].isspace():
                self.pos += 1
                continue

            m = RE_PHASES_MIDDOT_RANGE.match(text, self.pos)
            if m:
                p1, a, p2, b = m.group(1), m.group(2), m.group(3), m.group(4)
                phase = int(p1)
                self._mention(phase, m.group(0))
                self.pos = m.end()
                ref = Ref(kind="range", phase=phase, start=int(a), end=int(b), raw=m.group(0))
                self._add(ref)
                self._attach(ref, m.start())
                continue

            m = RE_PHASE.match(text, self.pos)
            if m:
                phase = int(m.group(1))
                self._mention(phase, m.group(0))
                self.pos = m.end()
                mm = RE_MIDDOT.match(text, self.pos)
                if mm:  # "Phase 6 · 04, 06"
                    self.pos = mm.end()
                    self._parse_items(phase)
                continue

            m = RE_LESSON_KW.match(text, self.pos)
            if m:
                self.pos = m.end()
                self._parse_items(self.sticky_phase)
                continue

            m = RE_TRACK.match(text, self.pos)
            if m:
                phase = self.sticky_phase if self.sticky_phase is not None else self.current_phase
                ref = Ref(kind="track", phase=phase, letter=m.group(1), raw=m.group(0))
                if self.mentions and self.mentions[-1].phase == phase:
                    self.mentions[-1].has_items = True
                    ref.mention = self.mentions[-1].mention
                self._add(ref)
                self.last_track = ref
                self.last_track_end = m.end()
                self.pos = m.end()
                continue

            m = RE_PAREN.match(text, self.pos)
            if m:
                content = m.group(1)
                self.pos = m.end()
                if self._paren_is_list(content):
                    # Parse the inside with the same state (sticky phase, mention)
                    inner = _Scanner(content, self.current_phase)
                    inner.sticky_phase = self.sticky_phase
                    inner.mentions = self.mentions
                    # The track word only "owns" the parenthetical list when
                    # nothing but filler separates them: "Track B foundations
                    # (lessons 20-29)" yes, "Track A, lessons 30; all of Phase 1
                    # (Lessons 01-04)" no.
                    if self.last_track is not None and not re.search(r"[,;]", self.text[self.last_track_end : m.start()]):
                        inner.last_track = self.last_track
                        inner.last_track_end = 0
                    else:
                        inner.last_track = None
                        inner.last_track_end = -1
                    if not RE_PAREN_HAS_LESSONS.search(content):
                        # "(04, 06, 07)" or "(20-29)": bare numbers, no keyword
                        inner._parse_items(inner.sticky_phase)
                    inner_res = inner.run()
                    # Inner items attach to our mention/track; copy them over.
                    for r in inner_res.refs:
                        if r.kind != "phase":
                            self._add(r)
                    self.result.unparsed.extend(inner_res.unparsed)
                    self.result.notes.extend(inner_res.notes)
                    if inner.last_track is not None and inner.last_track.adjacent_list:
                        self.last_track.adjacent_list = True  # type: ignore[union-attr]
                else:
                    self._flush_residue()
                    note = content.strip()
                    if self.last_ref is not None and not self.last_ref.note:
                        self.last_ref.note = note
                    else:
                        self.result.notes.append(note)
                continue

            m = RE_SEP.match(text, self.pos)
            if m:
                self.pos = m.end()
                self._flush_residue()
                continue

            m = RE_WORD.match(text, self.pos)
            if m:
                self.residue.append(m.group(0))
                self.pos = m.end()
                continue
            self.pos += 1  # unreachable in practice; guarantees progress

        self._flush_residue()
        # A phase mention that was followed by explicit lessons is a container,
        # not a requirement on the whole phase.
        self.result.refs = [r for r in self.result.refs if not (r.kind == "phase" and r.has_items)]
        return self.result


def parse_prereq_text(text: str | None, current_phase: int) -> ParseResult:
    """Pure parser. ``current_phase`` is the phase of the lesson being parsed."""
    if text is None:
        return ParseResult()
    stripped = text.strip()
    if not stripped or stripped.lower().rstrip(".") in {"none", "n/a", "-", "—"}:
        return ParseResult()
    return _Scanner(stripped, current_phase).run()


# --------------------------------------------------------------------------
# Resolution against the real lesson index
# --------------------------------------------------------------------------


def load_overrides(data_dir: Path) -> dict[str, Any]:
    path = data_dir / "prereq_overrides.json"
    if not path.is_file():
        return {}
    return {k: v for k, v in json.loads(path.read_text(encoding="utf-8")).items() if not k.startswith("_")}


def load_track_ranges(data_dir: Path) -> dict[tuple[int, str], tuple[int, int]]:
    path = data_dir / "tracks.json"
    if not path.is_file():
        return {}
    out: dict[tuple[int, str], tuple[int, int]] = {}
    for phase_str, letters in json.loads(path.read_text(encoding="utf-8")).items():
        if phase_str.startswith("_"):
            continue
        for letter, spec in letters.items():
            out[(int(phase_str), letter.upper())] = (spec["lessons"][0], spec["lessons"][1])
    return out


def resolve(
    parsed: ParseResult,
    *,
    lesson_node_id: str,
    current_phase: int,
    index: dict[int, list[int]],
    tracks: dict[tuple[int, str], tuple[int, int]],
    raw: str,
    source_file: str | None,
    line: int | None,
) -> tuple[list[Edge], list[str]]:
    """Turn refs into edges. Returns ``(edges, problems)``.

    Rules:
    * lesson  -> REQUIRES (confidence high)
    * range   -> one REQUIRES per existing lesson, sharing a ``group``;
                 if the range covers the whole phase -> one REQUIRES_PHASE
    * phase   -> REQUIRES_PHASE (confidence medium)
    * track   -> REQUIRES per lesson in ``tracks.json`` (confidence low,
                 because the source text is inconsistent about track ranges);
                 skipped when explicit numbers followed the track word
    * a reference to the lesson itself is dropped and reported
    """
    edges: list[Edge] = []
    problems: list[str] = []
    ctx = f"{lesson_node_id} ({source_file}:{line})"

    def mk(dst: str, etype: str, **attrs: Any) -> Edge:
        base = {"raw": raw, "via": "header"}
        base.update({k: v for k, v in attrs.items() if v not in (None, "")})
        return Edge(src=lesson_node_id, dst=dst, type=etype, attrs=base, source_file=source_file, line=line)

    for ref in parsed.refs:
        if ref.phase is None or ref.phase not in index:
            problems.append(f"{ctx}: unknown phase in {ref.raw!r}")
            continue
        existing = index[ref.phase]

        if ref.kind == "lesson":
            if ref.start not in existing:
                problems.append(f"{ctx}: lesson {ref.phase:02d}/{ref.start:02d} does not exist ({ref.raw!r})")
                continue
            dst = lesson_id(ref.phase, ref.start)
            if dst == lesson_node_id:
                problems.append(f"{ctx}: refers to itself ({ref.raw!r})")
                continue
            edges.append(mk(dst, "REQUIRES", confidence="high", span=ref.raw, note=ref.note))

        elif ref.kind == "range":
            lo, hi = sorted((ref.start, ref.end))
            nums = [n for n in existing if lo <= n <= hi]
            missing = sorted(set(range(lo, hi + 1)) - set(nums))
            if missing:
                problems.append(f"{ctx}: range {ref.raw!r} skips missing lessons {missing}")
            if not nums:
                continue
            if set(nums) == set(existing):
                edges.append(mk(phase_id(ref.phase), "REQUIRES_PHASE", confidence="medium", span=ref.raw, note=ref.note,
                                whole_phase=True))
                continue
            group = f"{ref.phase:02d}/{lo:02d}-{hi:02d}"
            for n in nums:
                dst = lesson_id(ref.phase, n)
                if dst == lesson_node_id:
                    continue
                edges.append(mk(dst, "REQUIRES", confidence="high", span=ref.raw, group=group, note=ref.note))

        elif ref.kind == "phase":
            if ref.phase == current_phase:
                # "All of Phase 14." written inside Phase 14 means "everything
                # before me in this phase": expand to the earlier lessons.
                own_num = int(lesson_node_id.rsplit("/", 1)[1])
                earlier = [n for n in existing if n < own_num]
                if not earlier:
                    problems.append(f"{ctx}: requires its own phase but is the first lesson ({ref.raw!r})")
                    continue
                for n in earlier:
                    edges.append(mk(lesson_id(ref.phase, n), "REQUIRES", confidence="medium", span=ref.raw,
                                    group=f"{ref.phase:02d}/{earlier[0]:02d}-{earlier[-1]:02d}", note="earlier lessons of this phase"))
                continue
            edges.append(mk(phase_id(ref.phase), "REQUIRES_PHASE", confidence="medium", span=ref.raw, note=ref.note))

        elif ref.kind == "track":
            if ref.adjacent_list:
                continue  # explicit numbers already produced the edges
            rng = tracks.get((ref.phase, ref.letter or ""))
            if rng is None:
                problems.append(f"{ctx}: unknown track {ref.raw!r} in phase {ref.phase}")
                continue
            group = f"Track {ref.letter}"
            for n in existing:
                if rng[0] <= n <= rng[1]:
                    dst = lesson_id(ref.phase, n)
                    if dst != lesson_node_id:
                        edges.append(mk(dst, "REQUIRES", confidence="low", span=ref.raw, group=group, note=ref.note,
                                        via="track"))
    return edges, problems


def apply_overrides(
    g: KnowledgeGraph, overrides: dict[str, Any], paths: Paths
) -> tuple[list[Edge], list[str]]:
    """``data/prereq_overrides.json``: add or drop edges the parser cannot infer.

    Shape::

        {"lesson:08/12": {"add": ["lesson:01/04"], "drop": [], "note": "why"}}
    """
    added: list[Edge] = []
    problems: list[str] = []
    src_file = paths.rel(paths.data_dir / "prereq_overrides.json")
    for lesson, spec in overrides.items():
        if lesson not in g:
            problems.append(f"overrides: unknown lesson {lesson}")
            continue
        for dst in spec.get("drop", []):
            before = len(g.edges)
            g.edges = [e for e in g.edges if not (e.src == lesson and e.dst == dst and e.type in ("REQUIRES", "REQUIRES_PHASE"))]
            g._edge_keys = {e.key() for e in g.edges}
            if len(g.edges) == before:
                problems.append(f"overrides: nothing to drop for {lesson} -> {dst}")
        for dst in spec.get("add", []):
            if dst not in g:
                problems.append(f"overrides: unknown target {dst} for {lesson}")
                continue
            etype = "REQUIRES_PHASE" if dst.startswith("phase:") else "REQUIRES"
            e = Edge(src=lesson, dst=dst, type=etype,
                     attrs={"confidence": "low", "via": "override", "note": spec.get("note", "")},
                     source_file=src_file, line=None)
            if g.add_edge(e):
                added.append(e)
    return added, problems


def extract_prereqs(g: KnowledgeGraph, paths: Paths) -> list[str]:
    """Parse every lesson's ``prereq_raw`` and add REQUIRES / REQUIRES_PHASE edges.

    Side effect on lesson nodes: ``prereq_unparsed`` (fragments the parser
    could not place) and ``prereq_notes`` are stored so the report and the
    vault can show them next to the lesson.
    """
    problems: list[str] = []
    from kg.extract.lessons import lesson_index  # local import avoids a cycle

    index = lesson_index(g)
    tracks = load_track_ranges(paths.data_dir)
    for node in g.nodes_of_type("lesson"):
        raw = node.attrs.get("prereq_raw")
        parsed = parse_prereq_text(raw, node.attrs["phase"])
        node.attrs["prereq_unparsed"] = parsed.unparsed
        node.attrs["prereq_notes"] = parsed.notes
        edges, probs = resolve(
            parsed,
            lesson_node_id=node.id,
            current_phase=node.attrs["phase"],
            index=index,
            tracks=tracks,
            raw=raw or "",
            source_file=node.source_file,
            line=node.attrs.get("prereq_line"),
        )
        problems.extend(probs)
        for e in edges:
            g.add_edge(e)
    _added, probs = apply_overrides(g, load_overrides(paths.data_dir), paths)
    problems.extend(probs)
    return problems
