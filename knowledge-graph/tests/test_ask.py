"""kg.graph_ops.ask / neighbors: the LLM-free query surface."""

from kg import graph_ops


def test_ask_returns_seeds_with_neighbourhoods(mini_graph):
    g, _, _ = mini_graph
    r = graph_ops.ask(g, "what do I need before multi-head attention?")
    ids = [s["id"] for s in r["seeds"]]
    assert ids[0] == "lesson:07/03"
    seed = r["seeds"][0]
    assert "REQUIRES" in seed["neighbors"]
    assert any(o == "lesson:07/02" for _d, o, _l in seed["neighbors"]["REQUIRES"])
    text = graph_ops.format_ask(r)
    assert "07/03 Multi-Head Attention" in text and "REQUIRES:" in text


def test_ask_matches_code_symbols_and_handles_no_match(mini_graph):
    g, _, _ = mini_graph
    r = graph_ops.ask(g, "where is SelfAttention defined")
    assert any(s["id"] == "lesson:07/02" for s in r["seeds"])
    assert graph_ops.ask(g, "zzzz qqqq")["seeds"] == []


def test_neighbors_groups_by_type(mini_graph):
    g, _, _ = mini_graph
    n = graph_ops.neighbors(g, "concept:attention")
    assert ("<-", "lesson:07/02") in n["TEACHES"]
    assert "RELATED_TO" in n and "IN_CATEGORY" in n
