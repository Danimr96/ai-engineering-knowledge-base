"""kg.extract.prereqs.resolve: refs -> edges against a known lesson index."""

from kg.extract.prereqs import parse_prereq_text, resolve

INDEX = {1: [1, 2, 3, 4], 7: [1, 2, 3], 19: [20, 21, 22, 30, 31]}
TRACKS = {(19, "A"): (20, 22)}


def run(raw, lesson="lesson:19/31", phase=19):
    parsed = parse_prereq_text(raw, phase)
    return resolve(parsed, lesson_node_id=lesson, current_phase=phase, index=INDEX, tracks=TRACKS,
                   raw=raw, source_file="f.md", line=7)


def test_single_lesson_high_confidence():
    edges, problems = run("Phase 7 · 02 (Self-Attention)")
    assert [(e.dst, e.type, e.attrs["confidence"]) for e in edges] == [("lesson:07/02", "REQUIRES", "high")]
    assert edges[0].attrs["note"] == "Self-Attention" and edges[0].attrs["span"] == "02"
    assert problems == []


def test_range_expands_and_shares_group():
    edges, problems = run("Phase 1, Lessons 01-03")
    assert [e.dst for e in edges] == ["lesson:01/01", "lesson:01/02", "lesson:01/03"]
    assert {e.attrs["group"] for e in edges} == {"01/01-03"}
    assert problems == []


def test_whole_phase_range_collapses_to_phase_edge():
    edges, _ = run("all of Phase 1 (Lessons 01-04)")
    assert [(e.dst, e.type) for e in edges] == [("phase:1", "REQUIRES_PHASE")]
    assert edges[0].attrs["whole_phase"] is True


def test_missing_lessons_are_reported_not_invented():
    edges, problems = run("Phase 7 · 09")
    assert edges == []
    assert any("07/09 does not exist" in p for p in problems)
    edges, problems = run("Phase 19 lessons 20-24")
    assert [e.dst for e in edges] == ["lesson:19/20", "lesson:19/21", "lesson:19/22"]
    assert any("skips missing lessons [23, 24]" in p for p in problems)


def test_self_reference_is_dropped():
    edges, problems = run("Lessons 30 and 31 of this phase")
    assert [e.dst for e in edges] == ["lesson:19/30"]
    assert any("refers to itself" in p for p in problems)


def test_own_phase_means_earlier_lessons():
    edges, problems = run("All of Phase 19.", lesson="lesson:19/30")
    assert [e.dst for e in edges] == ["lesson:19/20", "lesson:19/21", "lesson:19/22"]
    assert all(e.attrs["confidence"] == "medium" for e in edges)
    edges, problems = run("All of Phase 19.", lesson="lesson:19/20")
    assert edges == [] and any("first lesson" in p for p in problems)


def test_track_expands_only_without_explicit_numbers():
    edges, _ = run("Phase 19 Track A")
    assert [e.dst for e in edges] == ["lesson:19/20", "lesson:19/21", "lesson:19/22"]
    assert {e.attrs["confidence"] for e in edges} == {"low"} and {e.attrs["via"] for e in edges} == {"track"}
    edges, _ = run("Phase 19 Track A lessons 20-21")
    assert [e.dst for e in edges] == ["lesson:19/20", "lesson:19/21"]
    assert {e.attrs["confidence"] for e in edges} == {"high"}


def test_unknown_track_and_phase_are_problems():
    _, problems = run("Phase 19 Track E")  # only Track A exists in TRACKS
    assert any("unknown track" in p for p in problems)
    _, problems = run("Phase 42 · 01")
    assert any("unknown phase" in p for p in problems)
