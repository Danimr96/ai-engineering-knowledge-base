"""Lesson nodes, phase -> lesson CONTAINS edges, and Phase 19 tracks.

Sources
-------
* ``phases/NN-slug/MM-slug/`` folder names give the phase and lesson numbers
  (the stable part of the ID) and a fallback title.
* ``docs/en.md`` header block gives title, hook, Type, Languages,
  Prerequisites (kept raw here; parsed in ``prereqs.py``) and Time.
* ``code/`` file list and ``quiz.json`` question count become attributes.
* ``data/tracks.json`` (hand-maintained) groups Phase 19 lessons into the
  tracks that prerequisite strings refer to ("Track B foundations").

Pattern borrowed from upstream ``scripts/build_catalog.py`` (walk numbered
folders, read the H1), re-implemented so every line is ours.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from kg.extract.phases import iter_phase_dirs, slug_to_title
from kg.markdown import parse_lesson_header, parse_minutes
from kg.model import Edge, KnowledgeGraph, Node, lesson_id, phase_id, track_id
from kg.paths import Paths

LESSON_DIR_RE = re.compile(r"^(\d{2})-([a-z0-9][a-z0-9-]*)$")
CODE_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".mjs", ".rs", ".jl", ".go", ".swift", ".ipynb"}


def _languages(value: str | None) -> list[str]:
    """``'Python (stdlib), TypeScript'`` -> ``['Python', 'TypeScript']``.

    "none", "--" and "—" all mean "no code in this lesson".
    """
    if not value:
        return []
    value = re.sub(r"\([^)]*\)", "", value)  # drop qualifiers like "(stdlib)"
    langs = [v.strip() for v in re.split(r"[,/]| and ", value) if v.strip()]
    return [l for l in langs if l.lower() not in {"none", "--", "—", "-", "n/a"}]


def _lesson_type(value: str | None) -> str:
    """Normalise ``**Type:**`` to a small vocabulary.

    Upstream has 11 spellings ("Build", "Learn + Build", "Build (Capstone)",
    "Learn + lab", ...). We keep the raw string in ``type_raw`` and expose a
    normalised main type for filtering.
    """
    if not value:
        return "unknown"
    v = value.lower()
    if "capstone" in v:
        return "capstone"
    if "build" in v and "learn" in v:
        return "learn+build"
    if "build" in v:
        return "build"
    if "learn" in v:
        return "learn"
    if "reference" in v:
        return "reference"
    return v.strip()


def _code_files(code_dir: Path) -> list[str]:
    if not code_dir.is_dir():
        return []
    return sorted(
        p.relative_to(code_dir).as_posix()
        for p in code_dir.rglob("*")
        if p.is_file() and p.suffix in CODE_SUFFIXES and "__pycache__" not in p.parts
    )


def _quiz_count(quiz_path: Path) -> int:
    if not quiz_path.is_file():
        return 0
    try:
        data = json.loads(quiz_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return 0
    questions = data.get("questions") if isinstance(data, dict) else None
    return len(questions) if isinstance(questions, list) else 0


def iter_lesson_dirs(phase_dir: Path):
    for path in sorted(phase_dir.iterdir()):
        m = LESSON_DIR_RE.match(path.name)
        if path.is_dir() and m:
            yield int(m.group(1)), m.group(2), path


def build_lesson_node(paths: Paths, phase_num: int, lesson_num: int, slug: str, lesson_dir: Path) -> Node | None:
    docs = lesson_dir / "docs" / "en.md"
    code_files = _code_files(lesson_dir / "code")
    quiz_count = _quiz_count(lesson_dir / "quiz.json")
    if not docs.is_file() and not code_files and quiz_count == 0:
        return None  # an empty placeholder folder, not a lesson

    header = parse_lesson_header(docs.read_text(encoding="utf-8")) if docs.is_file() else None
    fields = header.fields if header else {}
    title = (header.title if header else None) or slug_to_title(slug)

    attrs: dict[str, Any] = {
        "phase": phase_num,
        "num": lesson_num,
        "ref": f"{phase_num:02d}/{lesson_num:02d}",
        "title": title,
        "slug": lesson_dir.name,
        "hook": header.hook if header else None,
        "lesson_type": _lesson_type(fields.get("Type")),
        "type_raw": fields.get("Type"),
        "languages": _languages(fields.get("Languages")),
        "time_min": parse_minutes(fields["Time"]) if fields.get("Time") else None,
        "prereq_raw": fields.get("Prerequisites"),
        "prereq_line": header.field_lines.get("Prerequisites") if header else None,
        "path": paths.rel(lesson_dir),
        "doc_path": paths.rel(docs) if docs.is_file() else None,
        "code_files": code_files,
        "quiz_count": quiz_count,
    }
    return Node(
        id=lesson_id(phase_num, lesson_num),
        type="lesson",
        label=f"{phase_num:02d}/{lesson_num:02d} {title}",
        attrs=attrs,
        source_file=paths.rel(docs) if docs.is_file() else paths.rel(lesson_dir),
        line=(header.title_line if header else None) or 1,
    )


def extract_lessons(g: KnowledgeGraph, paths: Paths) -> list[str]:
    """Add lesson nodes and CONTAINS edges. Returns problems."""
    problems: list[str] = []
    for phase_num, _slug, phase_dir in iter_phase_dirs(paths.phases_dir):
        if phase_id(phase_num) not in g:
            problems.append(f"phase folder {phase_dir.name} has no phase node (run extract_phases first)")
            continue
        order = 0
        for lesson_num, slug, lesson_dir in iter_lesson_dirs(phase_dir):
            node = build_lesson_node(paths, phase_num, lesson_num, slug, lesson_dir)
            if node is None:
                continue
            if node.id in g:
                problems.append(f"duplicate lesson number {node.id} ({lesson_dir.name})")
                continue
            g.add_node(node)
            order += 1
            g.add_edge(
                Edge(src=phase_id(phase_num), dst=node.id, type="CONTAINS", attrs={"order": order},
                     source_file=paths.rel(lesson_dir), line=None)
            )
    return problems


# --------------------------------------------------------------------------
# Tracks (Phase 19 only)
# --------------------------------------------------------------------------


def load_tracks(data_dir: Path) -> dict[str, dict[str, Any]]:
    """Read ``data/tracks.json``: ``{"19": {"A": {"title":..., "lessons":[20, 29]}}}``."""
    path = data_dir / "tracks.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def extract_tracks(g: KnowledgeGraph, paths: Paths) -> list[str]:
    problems: list[str] = []
    tracks = load_tracks(paths.data_dir)
    for phase_str, letters in tracks.items():
        if phase_str.startswith("_"):
            continue  # "_comment" keys
        phase_num = int(phase_str)
        for letter, spec in letters.items():
            start, end = spec["lessons"]
            tid = track_id(phase_num, letter)
            g.add_node(
                Node(
                    id=tid,
                    type="track",
                    label=f"Phase {phase_num} Track {letter}: {spec.get('title', '')}".strip(": "),
                    attrs={"phase": phase_num, "letter": letter, "title": spec.get("title"), "start": start, "end": end,
                           "note": spec.get("note")},
                    source_file=paths.rel(paths.data_dir / "tracks.json"),
                    line=None,
                )
            )
            order = 0
            for n in range(start, end + 1):
                lid = lesson_id(phase_num, n)
                if lid not in g:
                    problems.append(f"tracks.json: {tid} lists missing lesson {lid}")
                    continue
                order += 1
                g.add_edge(Edge(src=tid, dst=lid, type="CONTAINS", attrs={"order": order},
                                source_file=paths.rel(paths.data_dir / "tracks.json"), line=None))
    return problems


def lesson_index(g: KnowledgeGraph) -> dict[int, list[int]]:
    """``{phase_num: [lesson nums...]}`` — what actually exists on disk.

    The prerequisite resolver uses it to expand ranges and to flag references
    to lessons that do not exist.
    """
    index: dict[int, list[int]] = {}
    for n in g.nodes_of_type("lesson"):
        index.setdefault(n.attrs["phase"], []).append(n.attrs["num"])
    for nums in index.values():
        nums.sort()
    return index
