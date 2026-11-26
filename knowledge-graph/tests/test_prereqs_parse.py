"""kg.extract.prereqs.parse_prereq_text against real strings from the curriculum.

Each row: (raw text, phase of the lesson being parsed, expected refs, expected unparsed).
A ref is written compactly as:
    ("lesson", phase, num)  ("range", phase, lo, hi)  ("phase", phase)  ("track", phase, "B")
"""

import pytest

from kg.extract.prereqs import parse_prereq_text


def compact(ref):
    if ref.kind == "lesson":
        return ("lesson", ref.phase, ref.start)
    if ref.kind == "range":
        return ("range", ref.phase, ref.start, ref.end)
    if ref.kind == "phase":
        return ("phase", ref.phase)
    if ref.kind == "track":
        return ("track", ref.phase, ref.letter)
    raise AssertionError(ref)


CASES = [
    ("None", 5, [], []),
    ("", 5, [], []),
    ("Phase 7 · 02 (Self-Attention from Scratch)", 7, [("lesson", 7, 2)], []),
    ("Phase 1, Lessons 01-04", 2, [("range", 1, 1, 4)], []),
    ("Phase 1, Lesson 06 (Probability)", 2, [("lesson", 1, 6)], []),
    ("Phase 11 Lesson 01 (Prompt Engineering), Lesson 09 (Function Calling)", 13,
     [("lesson", 11, 1), ("lesson", 11, 9)], []),
    ("Lesson 03.02 (Multi-Layer Networks)", 3, [("lesson", 3, 2)], []),
    ("Lesson 03.06 (Optimizers), Lesson 03.08 (Weight Initialization)", 3, [("lesson", 3, 6), ("lesson", 3, 8)], []),
    ("Lessons 30 through 32 of this phase", 19, [("range", 19, 30, 32)], []),
    ("Lessons 30 and 31 of this phase", 19, [("lesson", 19, 30), ("lesson", 19, 31)], []),
    ("Phase 04 lessons, Phase 07 transformer lessons, Lessons 30 and 31 of this phase", 19,
     [("phase", 4), ("phase", 7), ("lesson", 19, 30), ("lesson", 19, 31)], []),
    ("Phase 6 · 04, 06, 07, 09, 10; Phase 2 · 09 (Model Evaluation)", 6,
     [("lesson", 6, 4), ("lesson", 6, 6), ("lesson", 6, 7), ("lesson", 6, 9), ("lesson", 6, 10), ("lesson", 2, 9)], []),
    ("Phases 14 · 32 to 14 · 40", 14, [("range", 14, 32, 40)], []),
    ("Phase 19 · 20-24 (Track A1: agent loop, tool registry), Phase 14 · 33 (instructions as constraints)", 19,
     [("range", 19, 20, 24), ("lesson", 14, 33)], []),
    ("Phase 18 · 07-09 (deception failures)", 18, [("range", 18, 7, 9)], []),
    ("Phase 13 · 22, 24, 25, and 26", 13, [("lesson", 13, 22), ("lesson", 13, 24), ("lesson", 13, 25), ("lesson", 13, 26)], []),
    ("Phase 14 lessons 47 and 51", 14, [("lesson", 14, 47), ("lesson", 14, 51)], []),
    ("Phase 13, Lessons 07, 09, and 10", 13, [("lesson", 13, 7), ("lesson", 13, 9), ("lesson", 13, 10)], []),
    ("Phase 13, Lessons 01 through 05", 13, [("range", 13, 1, 5)], []),
    ("Phase 2 Lesson 1-2 (What Is ML, Linear Regression)", 2, [("range", 2, 1, 2)], []),
    ("Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors, Matrices & Operations), 03 (Matrix Transformations)", 2,
     [("lesson", 1, 1), ("lesson", 1, 2), ("lesson", 1, 3)], []),
    ("Phase 1 (Lessons 09 Information Theory, 06 Probability)", 2, [("lesson", 1, 9), ("lesson", 1, 6)], []),
    ("Phase 1 (Lessons 08 Optimization, 14 Norms and Distances, 18 Convex Optimization)", 2,
     [("lesson", 1, 8), ("lesson", 1, 14), ("lesson", 1, 18)], []),
    ("Phase 1 (Lesson 14 Norms and Distances)", 2, [("lesson", 1, 14)], []),
    ("all of Phase 16 (Lessons 01-24)", 19, [("range", 16, 1, 24)], []),
    ("All of Phase 14.", 14, [("phase", 14)], []),
    ("All Phase 17 lessons covering engines (04, 06, 07, 09, 18)", 17,
     [("lesson", 17, 4), ("lesson", 17, 6), ("lesson", 17, 7), ("lesson", 17, 9), ("lesson", 17, 18)], []),
    ("All Phase 10 lessons 01-12", 19, [("range", 10, 1, 12)], []),
    ("Phase 10 (LLMs from Scratch), Phase 11 Lesson 01-02", 12, [("phase", 10), ("range", 11, 1, 2)], []),
    ("Phase 14 (Agent Engineering), Lesson 16.01 (Why Multi-Agent)", 16, [("phase", 14), ("lesson", 16, 1)], []),
    ("Phase 11, Phase 13, Phase 14, Phase 17, and Phase 18", 19,
     [("phase", 11), ("phase", 13), ("phase", 14), ("phase", 17), ("phase", 18)], []),
    ("Phase 19 Track C lessons 42-49", 19, [("track", 19, "C"), ("range", 19, 42, 49)], []),
    ("Phase 18 safety lessons, Phase 19 Track A lessons 25-29", 19, [("phase", 18), ("track", 19, "A"), ("range", 19, 25, 29)], []),
    ("Phase 19 Track B foundations, lessons 70 and 71", 19, [("track", 19, "B"), ("lesson", 19, 70), ("lesson", 19, 71)], []),
    ("Phase 19 Track B foundations", 19, [("track", 19, "B")], []),
    ("Phase 19 lessons 30-37 (Track B foundations)", 19, [("range", 19, 30, 37)], []),
    ("Phase 11 lessons 06 (RAG), 10 (evaluation); Phase 19 Track B foundations (lessons 20-29); Phase 19 lessons 64, 65", 19,
     [("lesson", 11, 6), ("lesson", 11, 10), ("track", 19, "B"), ("range", 19, 20, 29), ("lesson", 19, 64), ("lesson", 19, 65)], []),
    ("Phase 8 · 06 (DDPM), Phase 1 · Calculus", 8, [("lesson", 8, 6), ("phase", 1)], ["Calculus"]),
    ("Lesson 1 (Dev Environment), basic PyTorch familiarity", 0, [("lesson", 0, 1)], ["basic PyTorch familiarity"]),
    ("Phase 03 Lessons 01-10, basic NumPy", 3, [("range", 3, 1, 10)], ["basic NumPy"]),
    ("Phase 7 · 01 through 13. Don't skip.", 7, [("range", 7, 1, 13)], ["Don't skip"]),
    ("Phase 13 · 01 through 22, using MCP revision `2026-07-28`", 13, [("range", 13, 1, 22)], ["using MCP revision `2026-07-28`"]),
    ("Phase 0, Lessons 01 and 03", 0, [("lesson", 0, 1), ("lesson", 0, 3)], []),
    ("Phase 1, Lessons 01-04, 19 (complex numbers)", 2, [("range", 1, 1, 4), ("lesson", 1, 19)], []),
    ("Phase 12 · 05, Phase 8 (Generative AI)", 12, [("lesson", 12, 5), ("phase", 8)], []),
    ("Phase 1 · 06 (Vectors & Matrices), Phase 1 · 14 (Probability Distributions)", 2, [("lesson", 1, 6), ("lesson", 1, 14)], []),
]


@pytest.mark.parametrize("raw,phase,expected,unparsed", CASES, ids=[c[0][:40] or "empty" for c in CASES])
def test_parse(raw, phase, expected, unparsed):
    result = parse_prereq_text(raw, phase)
    assert [compact(r) for r in result.refs] == expected
    assert result.unparsed == unparsed


def test_track_adjacency_flag():
    r = parse_prereq_text("Phase 19 Track C lessons 42-49", 19)
    track = next(x for x in r.refs if x.kind == "track")
    assert track.adjacent_list is True
    r = parse_prereq_text("Phase 19 Track B foundations, lessons 70 and 71", 19)
    track = next(x for x in r.refs if x.kind == "track")
    assert track.adjacent_list is False
    r = parse_prereq_text("Phase 19 Track B foundations (lessons 20-29)", 19)
    track = next(x for x in r.refs if x.kind == "track")
    assert track.adjacent_list is True


def test_notes_are_kept():
    r = parse_prereq_text("Phase 7 · 02 (Self-Attention from Scratch), Phase 10 (LLMs from Scratch)", 11)
    assert r.refs[0].note == "Self-Attention from Scratch"
    assert r.refs[1].note == "LLMs from Scratch"
    r = parse_prereq_text("Phase 1 (Lessons 08 Optimization, 14 Norms and Distances)", 2)
    assert [x.note for x in r.refs] == ["Optimization", "Norms and Distances"]
