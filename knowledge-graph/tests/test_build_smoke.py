"""Integration test on the real curriculum (skipped if it is not checked out).

Asserts invariants and *ratchets*: lower bounds that only ever move up as the
parsers improve, rather than exact counts that break on every ``git pull``.
"""

import pytest

from kg.build import build_graph


@pytest.mark.slow
def test_real_repo_invariants(real):
    g, stats = build_graph(real)
    counts = g.node_counts()
    assert counts["phase"] == 20
    assert counts["lesson"] >= 523
    assert counts["concept"] >= 250
    assert sum(1 for n in g.nodes_of_type("concept") if n.attrs.get("canonical")) >= 250
    assert counts["artifact"] >= 400
    assert counts["learning_path"] >= 12

    assert stats.validation == []

    lessons = g.nodes_of_type("lesson")
    with_edges = {e.src for e in g.edges if e.type in ("REQUIRES", "REQUIRES_PHASE")}
    none_field = [n for n in lessons if (n.attrs.get("prereq_raw") or "").strip().lower().rstrip(".") == "none"]
    missing = [n.attrs["ref"] for n in lessons if n.attrs.get("prereq_raw") and n.id not in with_edges and n not in none_field]
    assert missing == [], f"lessons whose prerequisites produced no edge: {missing}"

    unparsed = sum(len(n.attrs.get("prereq_unparsed") or []) for n in lessons)
    assert unparsed <= 6, "ratchet: the parser got worse"

    problems = [p for stage, ps in stats.problems.items() for p in ps if stage not in ("learning_paths",)]
    assert len(problems) <= 3, problems

    kt = stats.key_terms
    assert kt.rows >= 3500
    assert kt.by_tier["exact"] + kt.by_tier["alias"] + kt.by_tier["normalized"] >= 330

    shared = {}
    for e in g.edges:
        if e.type == "CITES" and e.src.startswith("lesson:"):
            shared.setdefault(e.dst, set()).add(e.src)
    assert sum(1 for s in shared.values() if len(s) >= 2) >= 300, "resource canonicalisation regressed"
