"""kg.model: the container's guarantees."""

import json

import pytest

from kg.model import Edge, KnowledgeGraph, Node, lesson_id, parse_lesson_id, short_lesson_ref, iter_pairs


def _lesson(i: str) -> Node:
    return Node(id=i, type="lesson", label=i, attrs={})


def test_duplicate_node_is_an_error_unless_merge():
    g = KnowledgeGraph()
    g.add_node(Node(id="concept:x", type="concept", label="x", attrs={"a": 1}))
    with pytest.raises(ValueError):
        g.add_node(Node(id="concept:x", type="concept", label="x"))
    merged = g.add_node(Node(id="concept:x", type="concept", label="x", attrs={"a": 2, "b": 3}), merge=True)
    assert merged.attrs == {"a": 1, "b": 3}  # existing wins, missing filled


def test_unknown_types_are_rejected():
    g = KnowledgeGraph()
    with pytest.raises(ValueError):
        g.add_node(Node(id="x", type="Lesson", label="x"))
    g.add_node(_lesson("lesson:01/01"))
    with pytest.raises(ValueError):
        g.add_edge(Edge(src="lesson:01/01", dst="lesson:01/01", type="LIKES"))


def test_edge_dedupe_uses_via():
    g = KnowledgeGraph()
    g.add_node(_lesson("lesson:01/01"))
    g.add_node(Node(id="concept:a", type="concept", label="a"))
    assert g.add_edge(Edge("lesson:01/01", "concept:a", "TEACHES", {"via": "key_terms"}))
    assert not g.add_edge(Edge("lesson:01/01", "concept:a", "TEACHES", {"via": "key_terms"}))
    assert g.add_edge(Edge("lesson:01/01", "concept:a", "TEACHES", {"via": "glossary_learn_it"}))
    assert len(g.edges) == 2


def test_validate_reports_dangling_selfloop_and_type_mismatch():
    g = KnowledgeGraph()
    g.add_node(_lesson("lesson:01/01"))
    g.add_node(Node(id="phase:1", type="phase", label="p"))
    g.add_edge(Edge("lesson:01/01", "lesson:09/09", "REQUIRES"))  # dangling
    g.add_edge(Edge("lesson:01/01", "lesson:01/01", "REQUIRES"))  # self loop
    g.add_edge(Edge("phase:1", "lesson:01/01", "REQUIRES"))  # wrong source type
    g.add_edge(Edge("lesson:01/01", "phase:1", "REQUIRES_PHASE", {"confidence": "sure"}))  # bad confidence
    problems = g.validate()
    assert len(problems) == 4
    assert any("missing target" in p for p in problems)
    assert any("self-loop" in p for p in problems)
    assert any("expected ['lesson']" in p for p in problems)
    assert any("bad confidence" in p for p in problems)


def test_json_roundtrip_is_deterministic(tmp_path):
    g = KnowledgeGraph()
    g.add_node(_lesson("lesson:01/02"))
    g.add_node(_lesson("lesson:01/01"))
    g.add_edge(Edge("lesson:01/02", "lesson:01/01", "REQUIRES", {"confidence": "high"}, "f.md", 7))
    p = tmp_path / "g.json"
    g.write_json(p)
    first = p.read_text()
    g2 = KnowledgeGraph.read_json(p)
    assert list(g2.nodes) == ["lesson:01/01", "lesson:01/02"]  # read back in on-disk (sorted) order
    assert g2.edges[0].source_file == "f.md" and g2.edges[0].line == 7
    g2.write_json(p)
    assert p.read_text() == first
    data = json.loads(first)
    assert [n["id"] for n in data["nodes"]] == ["lesson:01/01", "lesson:01/02"]  # sorted on disk


def test_id_helpers():
    assert lesson_id(7, 3) == "lesson:07/03"
    assert parse_lesson_id("lesson:10/04") == (10, 4)
    assert short_lesson_ref("lesson:10/04") == "10/04"
    with pytest.raises(ValueError):
        parse_lesson_id("phase:1")
    assert list(iter_pairs([1, 2, 3])) == [(1, 2), (2, 3)]
    assert list(iter_pairs([])) == []
