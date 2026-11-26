"""kg.communities: label propagation is deterministic and labels are readable."""

from kg.communities import label_propagation


def test_label_propagation_finds_two_cliques():
    # two triangles joined by a single edge
    adj = {"a": {"b", "c"}, "b": {"a", "c"}, "c": {"a", "b", "d"},
           "d": {"c", "e", "f"}, "e": {"d", "f"}, "f": {"d", "e"}}
    labels = label_propagation(adj, seed=1)
    assert labels["a"] == labels["b"] == labels["c"]
    assert labels["d"] == labels["e"] == labels["f"]
    assert labels["a"] != labels["d"]
    assert label_propagation(adj, seed=1) == labels  # deterministic


def test_communities_on_fixture(mini_graph):
    g, _, _ = mini_graph
    comms = g.nodes_of_type("community")
    assert comms, "the mini graph should have at least one cluster of 4+"
    for c in comms:
        members = [e.src for e in g.edges if e.type == "IN_COMMUNITY" and e.dst == c.id]
        assert len(members) >= 4 and c.attrs["size"] == len(members)
        assert c.attrs["name"]  # a label built from concept names
        for m in members:
            assert g.get(m).attrs["community"] == c.attrs["num"]
    # the attention lessons and the attention concepts cluster together
    att = g.get("concept:attention").attrs.get("community")
    assert att is not None
    assert g.get("lesson:07/02").attrs.get("community") == att
