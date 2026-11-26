"""ROUTE_NEXT and BRIDGE edges from ``MY-LEARNING-PLAN.md``, plus progress evidence.

Source format::

    ## Route: Phase 10 core (about 20 h, plus bridges)

    | # | Lesson | Time | Bridges to check first |
    |---|---|---|---|
    | 10/04 | **Pre-training a mini GPT** ... | 120m | 01/05 chain rule · 03/03 backprop · ... |

Rules
-----
* Every table row whose first cell is ``NN/MM`` is a route step. Steps are
  chained in reading order across all route tables with ROUTE_NEXT edges.
* Every ``NN/MM`` token in the last column is a bridge: a BRIDGE edge from the
  route lesson to the bridge lesson, with the words after the token as note.
* Progress evidence is auto-detected: ``lessons/NN-MM-*.html`` (a visual
  lesson page exists) and ``learning-artifacts/NN-MM-*/`` (you built it).
  A lesson with evidence gets ``status: done``; a lesson on the route without
  evidence gets ``status: planned``. A ``status`` you set by hand in the vault
  note wins over both (see ``kg.obsidian.preserve``).
"""

from __future__ import annotations

import re

from kg.markdown import parse_tables, split_sections
from kg.model import Edge, KnowledgeGraph, iter_pairs, lesson_id
from kg.paths import Paths

_REF_RE = re.compile(r"(?<![\d/])(\d{2})/(\d{2})(?![\d/])")
_EVIDENCE_RE = re.compile(r"^(\d{2})-(\d{2})-")


def _ref_to_id(ref: str) -> str:
    p, l = ref.split("/")
    return lesson_id(int(p), int(l))


def extract_plan(g: KnowledgeGraph, paths: Paths) -> list[str]:
    problems: list[str] = []
    plan = paths.learning_plan
    if not plan.is_file():
        problems.append(f"learning plan not found: {plan}")
        _detect_progress(g, paths)
        return problems
    src = paths.rel(plan)
    text = plan.read_text(encoding="utf-8")

    route: list[str] = []  # lesson ids in reading order
    for sec in split_sections(text):
        if not sec.heading.lower().startswith("route"):
            continue
        for table in parse_tables(sec.lines, first_line_no=sec.start_line + 1):
            for row in table.rows:
                m = _REF_RE.fullmatch(row.cells[0].strip())
                if not m:
                    continue
                lid = _ref_to_id(m.group(0))
                if lid not in g:
                    problems.append(f"plan: route lesson {m.group(0)} does not exist ({src}:{row.line})")
                    continue
                node = g.get(lid)
                assert node is not None
                node.attrs["on_route"] = True
                node.attrs["route_order"] = len(route) + 1
                node.attrs["route_section"] = sec.heading
                node.attrs["route_note"] = row.cells[1].strip() if len(row.cells) > 1 else ""
                route.append(lid)

                bridges_cell = row.cells[-1] if len(row.cells) > 2 else ""
                for bm in _REF_RE.finditer(bridges_cell):
                    bid = _ref_to_id(bm.group(0))
                    if bid not in g:
                        problems.append(f"plan: bridge {bm.group(0)} does not exist ({src}:{row.line})")
                        continue
                    if bid == lid:
                        continue
                    # note = words after the token up to the next separator
                    rest = bridges_cell[bm.end():]
                    note = re.split(r"\s*[·|]\s*|\s{2,}", rest, maxsplit=1)[0].strip(" -–—:")
                    g.add_edge(Edge(src=lid, dst=bid, type="BRIDGE",
                                    attrs={"note": note, "confidence": "high", "via": "learning_plan"},
                                    source_file=src, line=row.line))

    for a, b in iter_pairs(route):
        g.add_edge(Edge(src=a, dst=b, type="ROUTE_NEXT", attrs={"via": "learning_plan"}, source_file=src, line=None))

    _detect_progress(g, paths)
    return problems


def _detect_progress(g: KnowledgeGraph, paths: Paths) -> None:
    evidence: dict[str, list[str]] = {}
    for folder, label in ((paths.visual_lessons_dir, "visual lesson"), (paths.learning_artifacts_dir, "artifact")):
        if not folder.is_dir():
            continue
        for entry in sorted(folder.iterdir()):
            m = _EVIDENCE_RE.match(entry.name)
            if not m:
                continue
            lid = lesson_id(int(m.group(1)), int(m.group(2)))
            evidence.setdefault(lid, []).append(f"{label}: {paths.rel(entry)}")
    for node in g.nodes_of_type("lesson"):
        ev = evidence.get(node.id, [])
        node.attrs["evidence"] = ev
        if ev:
            node.attrs["status"] = "done"
        elif node.attrs.get("on_route"):
            node.attrs["status"] = "planned"
        else:
            node.attrs["status"] = None
