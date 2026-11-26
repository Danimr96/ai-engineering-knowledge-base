"""kg.graph_ops on the mini graph."""

from kg import graph_ops


def test_prereqs_by_depth(mini_graph):
    g, _, _ = mini_graph
    layers = graph_ops.prereqs_of(g, "lesson:07/03")
    assert layers["lesson:07/02"] == 1
    assert layers["lesson:01/01"] == 2 and layers["lesson:01/02"] == 2 and layers["lesson:01/04"] == 2
    assert graph_ops.prereqs_of(g, "lesson:07/03", max_depth=1) == {"lesson:07/02": 1}


def test_bridges_count_as_prerequisites_but_can_be_excluded(mini_graph):
    g, _, _ = mini_graph
    assert graph_ops.prereqs_of(g, "lesson:19/30", max_depth=1)["lesson:07/02"] == 1  # via BRIDGE
    assert "lesson:07/02" not in graph_ops.prereqs_of(g, "lesson:19/30", max_depth=1, types=("REQUIRES",))
    assert graph_ops.prereqs_of(g, "lesson:19/30", types=("REQUIRES",))["lesson:07/02"] == 2  # via 19/20


def test_dependents_and_path(mini_graph):
    g, _, _ = mini_graph
    deps = graph_ops.dependents_of(g, "lesson:01/01")
    assert deps["lesson:01/02"] == 1 and deps["lesson:07/02"] == 1 and deps["lesson:07/03"] == 2
    assert graph_ops.path_between(g, "lesson:07/03", "lesson:01/01") == ["lesson:07/03", "lesson:07/02", "lesson:01/01"]
    assert graph_ops.path_between(g, "lesson:01/01", "lesson:07/03") is None


def test_concepts_and_search(mini_graph):
    g, _, _ = mini_graph
    assert graph_ops.shared_concepts(g, "lesson:07/02", "lesson:07/03") == ["concept:attention"]
    lessons = graph_ops.concept_lessons(g, "concept:attention")
    assert [l for l, _ in lessons] == ["lesson:07/02", "lesson:07/03"]
    assert graph_ops.concepts_of(g, "lesson:07/02")["concept:attention"] == "exact"
    hits = dict(graph_ops.search(g, "attention", types=("lesson",)))
    assert set(hits) == {"lesson:07/02", "lesson:07/03"}
    assert dict(graph_ops.search(g, "asr"))  # alias hit on the glossary concept
