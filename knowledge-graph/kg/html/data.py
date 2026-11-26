"""graph.json -> the payload the page loads at start-up.

What goes in, what stays out
----------------------------
``graph.json`` is 8 MB because every node and edge carries provenance and
every attribute the extractors found. The page needs a fraction of that, so
this module keeps an explicit allow-list per node type and per edge.

* **Provenance is dropped.** ``source_file`` and ``line`` matter when you
  audit the graph, not when you read a lesson.
* **Personal progress is dropped.** ``status``, ``evidence`` and the route
  fields describe one learner. The site is for many: each reader's progress
  lives in their own browser (``localStorage``).
* **The route is kept, as a path.** The route in ``MY-LEARNING-PLAN.md``
  (lessons plus the bridge lessons each one depends on) is useful to anyone,
  so it becomes one more learning path.

Shape
-----
Edges reference nodes by position, not by id, and edge types by position in
``edge_types``: ``[src_index, dst_index, type_index, attrs?]``. That halves
the size and the page rebuilds its lookup tables in a few milliseconds.

The transit-map look of the site needs one more thing the graph does not
have: which *line* (colour) each phase belongs to. That grouping is editorial,
so it lives in ``DEFAULT_LINES`` and can be overridden in ``data/site.json``.
"""

from __future__ import annotations

import json
from typing import Any

from kg.model import KnowledgeGraph, Node, parse_lesson_id
from kg.paths import Paths

SITE_CONFIG = "site.json"
ROUTE_PATH_ID = "path:learning-plan-route"

# name, light-theme colour, dark-theme colour, phases on the line
DEFAULT_LINES: list[dict[str, Any]] = [
    {"name": "Foundations", "color": "#1668c7", "dark": "#62adff", "phases": [0, 1, 2, 3]},
    {"name": "Vision, language, speech and RL", "color": "#178a4f", "dark": "#4fcf8a", "phases": [4, 5, 6, 9]},
    {"name": "Transformers and LLM internals", "color": "#7440d9", "dark": "#b294ff", "phases": [7, 8, 10]},
    {"name": "LLM engineering and tools", "color": "#c96a00", "dark": "#ffab45", "phases": [11, 12, 13]},
    {"name": "Agents and autonomy", "color": "#cf1f5a", "dark": "#ff7099", "phases": [14, 15, 16]},
    {"name": "Production and safety", "color": "#0a8a8d", "dark": "#42cfd2", "phases": [17, 18]},
    {"name": "Capstone projects", "color": "#22303f", "dark": "#dde6ee", "phases": [19]},
]

DEFAULT_SITE = {
    "title": "AI Engineering knowledge base",
    "tagline": "A complete AI engineering curriculum, mapped as a graph: what to learn, in what order, and why.",
}

# Attributes kept per node type. Anything else in ``attrs`` is not shipped.
NODE_ATTRS: dict[str, tuple[str, ...]] = {
    "phase": ("num", "title", "hours"),
    "lesson": (
        "phase", "num", "ref", "title", "hook", "lesson_type", "languages", "time_min",
        "quiz_count", "code_symbols", "community", "prereq_raw",
    ),
    "track": ("phase", "letter", "title", "start", "end", "note"),
    "concept": (
        "name", "canonical", "category", "aliases", "definition", "folk_definition",
        "why_it_matters", "in_practice", "confusion", "first_seen_in", "community",
    ),
    "category": ("name",),
    "artifact": ("name", "kind", "description", "tags", "lesson"),
    "resource": ("title", "url", "kind", "host"),
    "learning_path": ("key", "title", "summary", "kind", "minutes"),
    "myth": ("claim", "reality", "why_it_matters"),
    "library": ("name", "language"),
    "community": ("num", "name", "size", "lessons", "concepts", "phases", "main_phase"),
}

EDGE_ATTRS = (
    "confidence", "note", "via", "match", "term_as_written", "definition", "folk_definition",
    "order", "required", "minutes", "span", "whole_phase", "count",
)

# Edges that describe one learner's plan; replaced by the synthetic route path.
PERSONAL_EDGES = {"BRIDGE", "ROUTE_NEXT"}


def load_site_config(paths: Paths) -> dict[str, Any]:
    """``data/site.json`` merged over the defaults. The file is optional."""
    cfg: dict[str, Any] = {**DEFAULT_SITE, "lines": DEFAULT_LINES}
    path = paths.data_dir / SITE_CONFIG
    if path.is_file():
        cfg.update(json.loads(path.read_text(encoding="utf-8")))
    return cfg


def _slim(attrs: dict[str, Any], keep: tuple[str, ...]) -> dict[str, Any]:
    return {k: attrs[k] for k in keep if attrs.get(k) not in (None, "", [], {})}


def _lesson_sort_key(node_id: str) -> tuple[int, int]:
    return parse_lesson_id(node_id)


def _route_path(g: KnowledgeGraph) -> tuple[dict[str, Any], list[tuple[str, dict[str, Any]]]] | None:
    """The learning-plan route as a path: each lesson after its bridges.

    Returns the path node (already in payload form) and its ordered
    ``(lesson_id, edge_attrs)`` list, or ``None`` when no plan was overlaid.
    """
    route = sorted(
        (n for n in g.nodes_of_type("lesson") if n.attrs.get("on_route") and n.attrs.get("route_order") is not None),
        key=lambda n: n.attrs["route_order"],
    )
    if not route:
        return None
    steps: list[tuple[str, dict[str, Any]]] = []
    seen: set[str] = set()
    for lesson in route:
        for edge in sorted(g.out_edges(lesson.id, "BRIDGE"), key=lambda e: _lesson_sort_key(e.dst)):
            if edge.dst not in seen:
                seen.add(edge.dst)
                note = edge.attrs.get("note") or ""
                steps.append((edge.dst, {"required": False, "note": f"Bridge for {lesson.attrs['ref']}: {note}".rstrip(": ")}))
        if lesson.id not in seen:
            seen.add(lesson.id)
            steps.append((lesson.id, {"required": True}))
    minutes = sum((g.get(lid).attrs.get("time_min") or 0) for lid, _ in steps)  # type: ignore[union-attr]
    node = {
        "id": ROUTE_PATH_ID,
        "type": "learning_path",
        "label": "LLMs from scratch, with just-in-time bridges",
        "a": {
            "key": "learning-plan-route",
            "title": "LLMs from scratch, with just-in-time bridges",
            "summary": (
                "For people who already work with machine learning: go straight to how LLMs are built, "
                "and take a short bridge lesson from an earlier phase only right before the lesson that needs it."
            ),
            "kind": "custom-route",
            "minutes": minutes,
        },
    }
    return node, steps


def build_payload(g: KnowledgeGraph, paths: Paths, lessons_with_text: set[str]) -> dict[str, Any]:
    """Everything the page needs before the first click.

    ``lessons_with_text`` lists the lesson ids that have an on-demand payload,
    so the page knows whether a lesson page has content to load.
    """
    cfg = load_site_config(paths)
    nodes: list[dict[str, Any]] = []
    index: dict[str, int] = {}

    def add(node: dict[str, Any]) -> None:
        index[node["id"]] = len(nodes)
        nodes.append(node)

    def sort_key(n: Node) -> tuple[Any, ...]:
        if n.type == "lesson":
            return (n.type, *_lesson_sort_key(n.id))
        if n.type in ("phase", "community"):
            return (n.type, n.attrs.get("num", 0), 0)
        return (n.type, n.label.lower(), 0)

    for n in sorted(g, key=sort_key):
        attrs = _slim(n.attrs, NODE_ATTRS.get(n.type, ()))
        if n.type == "lesson" and n.id in lessons_with_text:
            attrs["text"] = 1
        add({"id": n.id, "type": n.type, "label": n.label, "a": attrs})

    edge_types = sorted({e.type for e in g.edges} - PERSONAL_EDGES)
    type_index = {t: i for i, t in enumerate(edge_types)}
    edges: list[list[Any]] = []
    for e in g.edges:
        if e.type in PERSONAL_EDGES or e.src not in index or e.dst not in index:
            continue
        row: list[Any] = [index[e.src], index[e.dst], type_index[e.type]]
        attrs = _slim(e.attrs, EDGE_ATTRS)
        if attrs:
            row.append(attrs)
        edges.append(row)

    route = _route_path(g)
    if route:
        node, steps = route
        add(node)
        if "INCLUDES" not in type_index:
            type_index["INCLUDES"] = len(edge_types)
            edge_types.append("INCLUDES")
        for order, (lesson, attrs) in enumerate(steps, 1):
            minutes = g.get(lesson).attrs.get("time_min")  # type: ignore[union-attr]
            edges.append([index[node["id"]], index[lesson], type_index["INCLUDES"], {"order": order, "minutes": minutes, **attrs}])

    # Which line each phase is on. Phases not listed share the last colours in turn.
    lines = [{"name": ln["name"], "color": ln["color"], "dark": ln.get("dark", ln["color"])} for ln in cfg["lines"]]
    phase_line: dict[str, int] = {}
    for i, ln in enumerate(cfg["lines"]):
        for num in ln.get("phases", []):
            phase_line[str(num)] = i
    for k, n in enumerate(sorted(g.nodes_of_type("phase"), key=lambda n: n.attrs["num"])):
        phase_line.setdefault(str(n.attrs["num"]), k % len(lines))

    return {
        "title": cfg["title"],
        "tagline": cfg["tagline"],
        "meta": {
            "built_at": g.meta.get("built_at"),
            "upstream_commit": g.meta.get("upstream_commit"),
        },
        "lines": lines,
        "phase_line": phase_line,
        "edge_types": edge_types,
        "nodes": nodes,
        "edges": edges,
    }
