"""End-to-end build on the mini fixture: every extractor's observable output."""

from kg.extract.resources import canonical_key


def edges(g, etype, src=None):
    return [e for e in g.edges if e.type == etype and (src is None or e.src == src)]


def test_phases_and_dag(mini_graph):
    g, stats, _ = mini_graph
    assert sorted(n.id for n in g.nodes_of_type("phase")) == ["phase:1", "phase:19", "phase:7"]
    p7 = g.get("phase:7")
    assert p7.attrs["title"] == "Transformers Deep Dive"  # from the phase README, not the folder
    assert p7.attrs["hours"] == 2.5  # from ROADMAP.md
    assert {(e.src, e.dst) for e in edges(g, "PHASE_REQUIRES")} == {("phase:7", "phase:1"), ("phase:19", "phase:7")}


def test_lessons_and_attributes(mini_graph):
    g, _, _ = mini_graph
    ids = sorted(n.id for n in g.nodes_of_type("lesson"))
    assert ids == ["lesson:01/01", "lesson:01/02", "lesson:01/04", "lesson:07/02", "lesson:07/03",
                   "lesson:19/20", "lesson:19/21", "lesson:19/30", "lesson:19/31", "lesson:19/32"]
    assert "lesson:19/99" not in g  # empty folder ignored
    l = g.get("lesson:07/02")
    assert l.attrs["title"] == "Self-Attention from Scratch"
    assert l.attrs["languages"] == ["Python", "TypeScript"]
    assert l.attrs["time_min"] == 90 and l.attrs["quiz_count"] == 2
    assert l.attrs["code_files"] == ["main.py", "tests/test_main.py"]
    assert g.get("lesson:01/02").attrs["languages"] == ["Python"]  # "(stdlib)" dropped
    assert g.get("lesson:01/01").attrs["languages"] == []  # "none"
    assert g.get("lesson:01/04").attrs["time_min"] == 60  # "1 hour"
    assert g.get("lesson:07/03").attrs["lesson_type"] == "learn+build"
    order = [e.dst for e in sorted(edges(g, "CONTAINS", "phase:7"), key=lambda e: e.attrs["order"])]
    assert order == ["lesson:07/02", "lesson:07/03"]


def test_tracks(mini_graph):
    g, _, _ = mini_graph
    assert g.get("track:19/A").attrs["title"] == "Harness track"
    assert [e.dst for e in edges(g, "CONTAINS", "track:19/A")] == ["lesson:19/20", "lesson:19/21"]


def test_prerequisite_edges(mini_graph):
    g, stats, _ = mini_graph
    req = {(e.src, e.dst): e for e in edges(g, "REQUIRES")}
    assert ("lesson:01/02", "lesson:01/01") in req
    assert ("lesson:07/02", "lesson:01/01") in req and ("lesson:07/02", "lesson:01/02") in req
    assert req[("lesson:07/02", "lesson:01/04")].attrs["via"] == "override"  # "Phase 1 · Calculus"
    assert ("lesson:07/03", "lesson:07/02") in req
    assert ("lesson:19/21", "lesson:19/20") in req
    # "Phase 19 Track A lessons 20-21": explicit numbers win over the track
    assert {d for s, d in req if s == "lesson:19/30"} == {"lesson:19/20", "lesson:19/21"}
    assert req[("lesson:19/30", "lesson:19/20")].attrs["confidence"] == "high"
    # "Lessons 20 and 21 of this phase"
    assert {d for s, d in req if s == "lesson:19/31"} == {"lesson:19/20", "lesson:19/21"}
    # "Phase 19 Track A, lessons 30 and 31; all of Phase 1 (Lessons 01-04)"
    e32 = {d for s, d in req if s == "lesson:19/32"}
    assert e32 == {"lesson:19/20", "lesson:19/21", "lesson:19/30", "lesson:19/31"}
    assert req[("lesson:19/32", "lesson:19/20")].attrs["confidence"] == "low"  # via track
    phase_edges = {(e.src, e.dst) for e in edges(g, "REQUIRES_PHASE")}
    assert ("lesson:19/32", "phase:1") in phase_edges  # 01-04 covers every phase-1 lesson on disk
    assert ("lesson:07/02", "phase:1") in phase_edges  # bare "Phase 1" before "· Calculus"
    assert g.get("lesson:07/02").attrs["prereq_unparsed"] == ["Calculus"]
    assert g.get("lesson:01/04").attrs["prereq_unparsed"] == ["basic NumPy"]
    assert stats.validation == []


def test_glossary_concepts(mini_graph):
    g, stats, _ = mini_graph
    canon = {n.attrs["name"] for n in g.nodes_of_type("concept") if n.attrs.get("canonical")}
    assert canon == {"Adam (Optimizer)", "Attention", "Automatic Speech Recognition (ASR)", "KV Cache", "Self-Attention", "Softmax"}
    assert {n.label for n in g.nodes_of_type("category")} == {"Math & training", "Models & inference", "Multimodal systems"}
    rel = {(e.src, e.dst) for e in edges(g, "RELATED_TO")}
    assert ("concept:attention", "concept:kv-cache") in rel
    assert ("concept:softmax", "concept:adam-optimizer") in rel
    learn = [e for e in edges(g, "TEACHES") if e.attrs["via"] == "glossary_learn_it"]
    assert {(e.src, e.dst) for e in learn} == {("lesson:07/02", "concept:attention"), ("lesson:07/02", "concept:self-attention")}
    assert g.get("concept:kv-cache").attrs["aliases"] == ["KV-cache", "key-value cache"]
    assert g.get("myth:1").attrs["claim"] == "Bigger is always better"
    assert stats.problems["glossary"] == []


def test_key_terms_matching(mini_graph):
    g, stats, _ = mini_graph
    kt = stats.key_terms
    assert kt.lessons_with_table == 4 and kt.rows == 11
    teaches = {(e.src, e.dst): e for e in edges(g, "TEACHES") if e.attrs["via"] == "key_terms"}
    assert teaches[("lesson:07/03", "concept:attention")].attrs["match"] == "exact"
    assert teaches[("lesson:07/03", "concept:kv-cache")].attrs["match"] == "exact"
    assert teaches[("lesson:07/03", "concept:attention")].attrs["definition"] == "Weighted average."
    # "MHA" -> Attention through data/aliases.json
    assert ("lesson:07/03", "concept:attention") in teaches
    assert kt.by_tier["alias"] >= 1
    # non-canonical concepts merge across lessons, acronym kept as alias
    gqa = g.get("concept:grouped-query-attention")
    assert gqa is not None and gqa.attrs["canonical"] is False and gqa.attrs["aliases"] == ["GQA"]
    dot = g.get("concept:dot-product")
    assert dot.attrs["first_seen_in"] == "01/02"
    # the escaped-pipe row survived as one term
    assert "concept:p-token-context" in g
    # 2-column header: last column is the definition
    assert g.get("concept:vector").attrs["definition"] == "An ordered list of numbers."


def test_artifacts(mini_graph):
    g, _, _ = mini_graph
    arts = {n.attrs["name"]: n for n in g.nodes_of_type("artifact")}
    assert set(arts) == {"mha-configurator", "mha-bundle"}
    assert arts["mha-configurator"].attrs["tags"] == ["transformers", "attention"]
    assert arts["mha-bundle"].attrs["bundle"] is True
    assert {e.dst for e in edges(g, "SHIPS", "lesson:07/03")} == {n.id for n in arts.values()}


def test_resources_are_canonical(mini_graph):
    g, _, _ = mini_graph
    r = g.get("resource:arxiv:1706.03762")
    assert r is not None and r.attrs["kind"] == "arxiv"
    citing = {e.src for e in edges(g, "CITES") if e.dst == r.id}
    assert citing == {"lesson:07/02", "lesson:07/03"}  # /abs/ and /pdf/...v7 merged
    blog = g.get("resource:jalammar.github.io/illustrated-transformer")
    assert blog is not None  # www. and utm_source stripped
    adam = g.get("resource:arxiv:1412.6980")
    assert {e.src for e in edges(g, "CITES") if e.dst == adam.id} == {"concept:adam-optimizer"}


def test_canonical_key_cases():
    assert canonical_key("https://arxiv.org/pdf/1706.03762v7") == ("arxiv:1706.03762", "arxiv")
    assert canonical_key("http://ARXIV.org/abs/1706.03762") == ("arxiv:1706.03762", "arxiv")
    assert canonical_key("https://doi.org/10.1000/ABC/") == ("doi:10.1000/abc", "doi")
    assert canonical_key("https://www.Example.com/a/b/?utm_source=x&q=1#top") == ("example.com/a/b?q=1", "web")


def test_learning_paths(mini_graph):
    g, stats, _ = mini_graph
    p = g.get("path:mini-path")
    assert p.attrs["minutes"] == 150
    inc = {e.dst: e for e in edges(g, "INCLUDES", p.id)}
    assert set(inc) == {"lesson:07/02", "lesson:07/03", "lesson:01/04"}
    assert inc["lesson:07/02"].attrs["required"] is True and inc["lesson:01/04"].attrs["required"] is False
    assert any("missing lesson lesson:99/01" in p for p in stats.problems["learning_paths"])


def test_plan_overlay_and_progress(mini_graph):
    g, stats, _ = mini_graph
    route = sorted(((n.attrs["route_order"], n.id) for n in g.nodes_of_type("lesson") if n.attrs.get("on_route")))
    assert route == [(1, "lesson:07/02"), (2, "lesson:07/03"), (3, "lesson:19/30")]
    assert g.get("lesson:01/04").attrs.get("on_route") is None  # "Not a route" section ignored
    assert [(e.src, e.dst) for e in edges(g, "ROUTE_NEXT")] == [("lesson:07/02", "lesson:07/03"), ("lesson:07/03", "lesson:19/30")]
    bridges = {(e.src, e.dst): e.attrs["note"] for e in edges(g, "BRIDGE")}
    assert bridges == {("lesson:07/02", "lesson:01/01"): "linear algebra", ("lesson:07/02", "lesson:01/02"): "vectors",
                       ("lesson:19/30", "lesson:07/02"): "attention"}
    assert g.get("lesson:07/02").attrs["status"] == "done"  # learning-artifacts/07-02-*
    assert g.get("lesson:07/03").attrs["status"] == "done"  # lessons/07-03-*.html
    assert g.get("lesson:19/30").attrs["status"] == "planned"
    assert g.get("lesson:01/01").attrs["status"] is None
    assert stats.problems["plan"] == []
