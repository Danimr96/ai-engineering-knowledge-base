"""The graph model: nodes, edges, and the container that validates them.

Why this module exists
----------------------
A knowledge graph is only useful if every producer (the extractors) and every
consumer (the report, the CLI, the Obsidian writer) agree on the same shapes.
This module is that agreement. It is deliberately small and dependency-free:
two dataclasses and one container class you can read top to bottom.

Design decisions worth knowing
------------------------------
* **Property graph.** Nodes and edges both carry a free-form ``attrs`` dict.
  That is the same model Neo4j uses, so the graph can later be loaded there
  without reshaping.
* **IDs are stable, not pretty.** ``lesson:10/04`` is built from the numeric
  folder prefixes, never from slugs, because upstream may rename a folder but
  will not renumber it. The human-readable name lives in ``label``.
* **Provenance on everything.** ``source_file`` and ``line`` say which file and
  line produced a node or edge, so any surprising fact in the vault can be
  traced back to the markdown that produced it.
* **Validation is explicit.** ``KnowledgeGraph.validate()`` returns a list of
  problems instead of raising, so the report can show all of them at once.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator

# --------------------------------------------------------------------------
# Vocabulary. Adding a new type means adding it here first, so the validator
# catches typos like "Lesson" vs "lesson" in an extractor.
# --------------------------------------------------------------------------

NODE_TYPES = frozenset(
    {
        "phase",
        "lesson",
        "track",
        "concept",
        "category",
        "artifact",
        "resource",
        "learning_path",
        "myth",
        "library",
        "community",
    }
)

# Each edge type says which node types it may connect. ``None`` means any.
EDGE_TYPES: dict[str, tuple[frozenset[str] | None, frozenset[str] | None]] = {
    "CONTAINS": (frozenset({"phase", "track"}), frozenset({"lesson"})),
    "PHASE_REQUIRES": (frozenset({"phase"}), frozenset({"phase"})),
    "REQUIRES": (frozenset({"lesson"}), frozenset({"lesson"})),
    "REQUIRES_PHASE": (frozenset({"lesson"}), frozenset({"phase"})),
    "TEACHES": (frozenset({"lesson"}), frozenset({"concept"})),
    "RELATED_TO": (frozenset({"concept"}), frozenset({"concept"})),
    "IN_CATEGORY": (frozenset({"concept"}), frozenset({"category"})),
    "SHIPS": (frozenset({"lesson"}), frozenset({"artifact"})),
    "CITES": (frozenset({"lesson", "concept"}), frozenset({"resource"})),
    "INCLUDES": (frozenset({"learning_path"}), frozenset({"lesson"})),
    "BRIDGE": (frozenset({"lesson"}), frozenset({"lesson"})),
    "ROUTE_NEXT": (frozenset({"lesson"}), frozenset({"lesson"})),
    "USES": (frozenset({"lesson"}), frozenset({"library"})),
    "IN_COMMUNITY": (frozenset({"lesson", "concept"}), frozenset({"community"})),
}

CONFIDENCE_LEVELS = ("high", "medium", "low")


# --------------------------------------------------------------------------
# Data classes
# --------------------------------------------------------------------------


@dataclass
class Node:
    """One entity in the graph.

    ``label`` is what a human sees (note title, graph label). ``attrs`` holds
    everything else and is copied verbatim into the note's frontmatter.
    """

    id: str
    type: str
    label: str
    attrs: dict[str, Any] = field(default_factory=dict)
    source_file: str | None = None
    line: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "label": self.label,
            "attrs": self.attrs,
            "source_file": self.source_file,
            "line": self.line,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Node":
        return cls(
            id=d["id"],
            type=d["type"],
            label=d["label"],
            attrs=dict(d.get("attrs") or {}),
            source_file=d.get("source_file"),
            line=d.get("line"),
        )


@dataclass
class Edge:
    """A directed, typed relationship between two node IDs."""

    src: str
    dst: str
    type: str
    attrs: dict[str, Any] = field(default_factory=dict)
    source_file: str | None = None
    line: int | None = None

    def key(self) -> tuple[str, str, str, str, str]:
        """Identity used for de-duplication.

        Two edges are "the same" when they connect the same nodes with the same
        type *and* the same evidence: the same ``via`` (Key Terms table vs.
        glossary "Learn it") and, for Key Terms, the same spelling of the term.
        A lesson whose table lists both "MHA" and "Attention" and maps both to
        the glossary's Attention keeps two edges, because those are two rows.
        """
        return (self.src, self.dst, self.type, str(self.attrs.get("via", "")), str(self.attrs.get("term_as_written", "")))

    def to_dict(self) -> dict[str, Any]:
        return {
            "src": self.src,
            "dst": self.dst,
            "type": self.type,
            "attrs": self.attrs,
            "source_file": self.source_file,
            "line": self.line,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Edge":
        return cls(
            src=d["src"],
            dst=d["dst"],
            type=d["type"],
            attrs=dict(d.get("attrs") or {}),
            source_file=d.get("source_file"),
            line=d.get("line"),
        )


# --------------------------------------------------------------------------
# Container
# --------------------------------------------------------------------------


class KnowledgeGraph:
    """In-memory graph with de-duplication, lookup indexes and validation."""

    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []
        self._edge_keys: set[tuple[str, str, str, str]] = set()
        self.meta: dict[str, Any] = {}

    # ---- adding -------------------------------------------------------
    def add_node(self, node: Node, *, merge: bool = False) -> Node:
        """Insert a node.

        With ``merge=False`` (the default) a duplicate ID is an error: two
        extractors claiming the same entity usually means an ID-scheme bug.
        With ``merge=True`` the existing node wins and only *missing* attrs
        are filled in. Concepts use ``merge`` because the same key term shows
        up in many lessons and we want exactly one node for it.
        """
        if node.type not in NODE_TYPES:
            raise ValueError(f"unknown node type {node.type!r} for {node.id}")
        existing = self.nodes.get(node.id)
        if existing is None:
            self.nodes[node.id] = node
            return node
        if not merge:
            raise ValueError(f"duplicate node id {node.id!r}")
        for k, v in node.attrs.items():
            existing.attrs.setdefault(k, v)
        return existing

    def add_edge(self, edge: Edge) -> bool:
        """Insert an edge; returns False if an identical one already exists."""
        if edge.type not in EDGE_TYPES:
            raise ValueError(f"unknown edge type {edge.type!r} ({edge.src} -> {edge.dst})")
        k = edge.key()
        if k in self._edge_keys:
            return False
        self._edge_keys.add(k)
        self.edges.append(edge)
        return True

    # ---- lookup -------------------------------------------------------
    def get(self, node_id: str) -> Node | None:
        return self.nodes.get(node_id)

    def __contains__(self, node_id: str) -> bool:
        return node_id in self.nodes

    def nodes_of_type(self, node_type: str) -> list[Node]:
        return [n for n in self.nodes.values() if n.type == node_type]

    def out_edges(self, node_id: str, edge_type: str | None = None) -> list[Edge]:
        return [
            e for e in self.edges if e.src == node_id and (edge_type is None or e.type == edge_type)
        ]

    def in_edges(self, node_id: str, edge_type: str | None = None) -> list[Edge]:
        return [
            e for e in self.edges if e.dst == node_id and (edge_type is None or e.type == edge_type)
        ]

    def adjacency(self, edge_type: str) -> dict[str, list[str]]:
        """``{src: [dst, ...]}`` for one edge type. Used by the BFS helpers.

        Building this once per traversal is O(E); scanning ``self.edges`` for
        every neighbour lookup would make BFS O(V * E).
        """
        adj: dict[str, list[str]] = defaultdict(list)
        for e in self.edges:
            if e.type == edge_type:
                adj[e.src].append(e.dst)
        return adj

    def edge_counts(self) -> dict[str, int]:
        counts: dict[str, int] = defaultdict(int)
        for e in self.edges:
            counts[e.type] += 1
        return dict(sorted(counts.items()))

    def node_counts(self) -> dict[str, int]:
        counts: dict[str, int] = defaultdict(int)
        for n in self.nodes.values():
            counts[n.type] += 1
        return dict(sorted(counts.items()))

    # ---- validation ---------------------------------------------------
    def validate(self) -> list[str]:
        """Return human-readable problems. An empty list means the graph is sound.

        Checks:
        * every edge endpoint exists (no dangling references);
        * endpoint types match the vocabulary in ``EDGE_TYPES``;
        * no self-loops on prerequisite edges (a lesson requiring itself is
          always a parsing bug);
        * confidence values, when present, are from ``CONFIDENCE_LEVELS``.
        """
        problems: list[str] = []
        for e in self.edges:
            src, dst = self.nodes.get(e.src), self.nodes.get(e.dst)
            if src is None:
                problems.append(f"{e.type}: missing source node {e.src!r} (from {e.source_file}:{e.line})")
                continue
            if dst is None:
                problems.append(f"{e.type}: missing target node {e.dst!r} (from {e.source_file}:{e.line})")
                continue
            allowed_src, allowed_dst = EDGE_TYPES[e.type]
            if allowed_src is not None and src.type not in allowed_src:
                problems.append(f"{e.type}: source {e.src!r} has type {src.type!r}, expected {sorted(allowed_src)}")
            if allowed_dst is not None and dst.type not in allowed_dst:
                problems.append(f"{e.type}: target {e.dst!r} has type {dst.type!r}, expected {sorted(allowed_dst)}")
            if e.type in ("REQUIRES", "BRIDGE", "ROUTE_NEXT") and e.src == e.dst:
                problems.append(f"{e.type}: self-loop on {e.src!r} (from {e.source_file}:{e.line})")
            conf = e.attrs.get("confidence")
            if conf is not None and conf not in CONFIDENCE_LEVELS:
                problems.append(f"{e.type}: bad confidence {conf!r} on {e.src} -> {e.dst}")
        return problems

    # ---- (de)serialisation --------------------------------------------
    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "meta": self.meta,
            "nodes": [n.to_dict() for n in sorted(self.nodes.values(), key=lambda n: n.id)],
            "edges": [e.to_dict() for e in sorted(self.edges, key=lambda e: (e.type, e.src, e.dst))],
        }

    def write_json(self, path: Path) -> None:
        """Write ``graph.json`` deterministically (sorted keys, sorted nodes).

        Determinism matters: if nothing changed upstream, a rebuild produces a
        byte-identical file, so a ``diff`` shows exactly what a change did.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(self.to_dict(), indent=1, ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "KnowledgeGraph":
        g = cls()
        g.meta = dict(d.get("meta") or {})
        for nd in d.get("nodes", []):
            g.add_node(Node.from_dict(nd))
        for ed in d.get("edges", []):
            g.add_edge(Edge.from_dict(ed))
        return g

    @classmethod
    def read_json(cls, path: Path) -> "KnowledgeGraph":
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))

    # ---- misc ---------------------------------------------------------
    def __len__(self) -> int:
        return len(self.nodes)

    def __iter__(self) -> Iterator[Node]:
        return iter(self.nodes.values())


# --------------------------------------------------------------------------
# ID helpers. Keeping them here (not scattered across extractors) is what
# guarantees two modules never disagree on how to spell the same ID.
# --------------------------------------------------------------------------


def phase_id(num: int) -> str:
    return f"phase:{num}"


def lesson_id(phase: int, lesson: int) -> str:
    return f"lesson:{phase:02d}/{lesson:02d}"


def track_id(phase: int, letter: str) -> str:
    return f"track:{phase:02d}/{letter.upper()}"


def concept_id(normalized_name: str) -> str:
    return f"concept:{normalized_name}"


def category_id(slug: str) -> str:
    return f"category:{slug}"


def artifact_id(phase: int, lesson: int, name: str) -> str:
    return f"artifact:{phase:02d}/{lesson:02d}/{name}"


def resource_id(canonical: str) -> str:
    return f"resource:{canonical}"


def learning_path_id(path_key: str) -> str:
    return f"path:{path_key}"


def myth_id(n: int) -> str:
    return f"myth:{n}"


def parse_lesson_id(node_id: str) -> tuple[int, int]:
    """``'lesson:10/04'`` -> ``(10, 4)``. Raises ValueError on anything else."""
    if not node_id.startswith("lesson:"):
        raise ValueError(f"not a lesson id: {node_id!r}")
    p, l = node_id[len("lesson:") :].split("/")
    return int(p), int(l)


def short_lesson_ref(node_id: str) -> str:
    """``'lesson:10/04'`` -> ``'10/04'``, the form used in MY-LEARNING-PLAN.md."""
    p, l = parse_lesson_id(node_id)
    return f"{p:02d}/{l:02d}"


def iter_pairs(items: Iterable[Any]) -> Iterator[tuple[Any, Any]]:
    """Consecutive pairs: [a, b, c] -> (a, b), (b, c). Used for ROUTE_NEXT."""
    it = iter(items)
    try:
        prev = next(it)
    except StopIteration:
        return
    for cur in it:
        yield prev, cur
        prev = cur
