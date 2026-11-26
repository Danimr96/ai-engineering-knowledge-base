import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evals_core import check_qualifier, diff_ci, gate, wilson_ci


class TestWilson(unittest.TestCase):
    def test_no_cases_means_no_knowledge(self):
        self.assertEqual(wilson_ci(0, 0), (0.0, 1.0))

    def test_five_green_scenarios(self):
        lo, hi = wilson_ci(5, 5)
        self.assertAlmostEqual(lo, 0.5655, places=3)
        self.assertAlmostEqual(hi, 1.0, places=6)

    def test_ninety_of_hundred(self):
        lo, hi = wilson_ci(90, 100)
        self.assertAlmostEqual(lo, 0.8256, places=3)
        self.assertAlmostEqual(hi, 0.9448, places=3)

    def test_zero_passes_is_not_zero_width(self):
        lo, hi = wilson_ci(0, 10)
        self.assertAlmostEqual(lo, 0.0, places=6)
        self.assertAlmostEqual(hi, 0.2775, places=3)

    def test_more_cases_narrow_the_interval(self):
        w50 = wilson_ci(45, 50)[1] - wilson_ci(45, 50)[0]
        w200 = wilson_ci(180, 200)[1] - wilson_ci(180, 200)[0]
        self.assertLess(w200, w50)


class TestDiffAndGate(unittest.TestCase):
    def test_diff_interval_values(self):
        lo, d, hi = diff_ci(188, 200, 176, 200)
        self.assertAlmostEqual(d, -0.06, places=6)
        self.assertAlmostEqual(lo, -0.1182, places=3)
        self.assertAlmostEqual(hi, -0.0034, places=3)

    def test_five_vs_five_is_inconclusive(self):
        self.assertEqual(gate(5, 5, 5, 5), "INCONCLUSIVE")

    def test_clear_regression_blocks(self):
        self.assertEqual(gate(188, 200, 176, 200), "BLOCK")

    def test_small_drop_small_n_is_inconclusive(self):
        self.assertEqual(gate(180, 200, 176, 200), "INCONCLUSIVE")

    def test_equal_quality_large_n_ships(self):
        self.assertEqual(gate(900, 1000, 905, 1000), "SHIP")

    def test_block_wins_over_ship(self):
        self.assertEqual(gate(495, 500, 480, 500, margin=0.10), "BLOCK")


class TestCheckQualifier(unittest.TestCase):
    EXPECTED = {"score": 85, "category": "caliente", "state": "cualificado"}

    def test_within_tolerance_passes(self):
        actual = {"score": 81, "category": "caliente", "state": "cualificado"}
        self.assertEqual(check_qualifier(self.EXPECTED, actual), [])

    def test_several_failures_sorted(self):
        actual = {"score": 60, "category": "tibio", "state": "cualificado"}
        self.assertEqual(check_qualifier(self.EXPECTED, actual), ["category", "score"])

    def test_opt_out_violation(self):
        expected = {"score": 20, "category": "frio", "state": "opt_out", "opt_out": True}
        actual = {"score": 20, "category": "frio", "state": "opt_out", "messages_after_opt_out": 1}
        self.assertEqual(check_qualifier(expected, actual), ["opt_out"])


if __name__ == "__main__":
    unittest.main()
