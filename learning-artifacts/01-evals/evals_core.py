"""Lesson 01 · Evals — your implementation.

Fill in each function until every test passes:
    cd "learning-artifacts/01-evals"
    ../../ai-engineering-from-scratch/.venv/bin/python -m unittest discover tests -v

Rules: write it yourself. Ask Claude for hints or a review, not for the code.
Formulas are on the lesson page (lessons/01-evals.html).
"""
import math


def wilson_ci(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval for a pass rate.

    Returns (lower, upper), clamped to [0, 1].
    total == 0 -> (0.0, 1.0): with no cases, we know nothing.
    """
    raise NotImplementedError


def diff_ci(base_pass: int, base_n: int, new_pass: int, new_n: int,
            z: float = 1.96) -> tuple[float, float, float]:
    """Newcombe interval for d = p_new - p_base, built from two Wilson intervals.

    Returns (lower, d, upper).
    """
    raise NotImplementedError


def gate(base_pass: int, base_n: int, new_pass: int, new_n: int,
         margin: float = 0.03) -> str:
    """Regression gate for a prompt/model change.

    Checked in this order:
      "BLOCK"        if the new version is confidently worse (upper < 0)
      "SHIP"         if it is confidently not worse by more than `margin` (lower > -margin)
      "INCONCLUSIVE" otherwise (you need more cases)
    """
    raise NotImplementedError


def check_qualifier(expected: dict, actual: dict, score_tolerance: int = 5) -> list[str]:
    """Deterministic assertions for one D'Garage golden scenario.

    Return the sorted names of the checks that FAILED ([] means pass):
      "score"    -> abs(actual["score"] - expected["score"]) > score_tolerance
      "category" -> categories differ
      "state"    -> states differ
      "opt_out"  -> expected.get("opt_out") is True and actual["messages_after_opt_out"] > 0
    """
    raise NotImplementedError
