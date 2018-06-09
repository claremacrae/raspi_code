import unittest

from approvaltests import verify_all_combinations
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory

import sys
sys.path.append("..")
from TinyPirate import mixer, constrain

class TinyPirateTest(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get_first_working()

    def test_mixer(self):
        x_axis_values = [n for n in range(-140, 141, 2)]
        y_axis_values = [n for n in range(-140, 141, 2)]

        arg_combinations = (x_axis_values, y_axis_values)
        func = lambda a, b: mixer(a, b)
        verify_all_combinations(
            func,
            arg_combinations,
            reporter=self.reporter)

    def test_constrain(self):
        values = [n for n in range(-140, 141)]

        arg_combinations = (values,)
        func = lambda a: constrain(a, -125, 125)
        verify_all_combinations(
            func,
            arg_combinations,
            reporter=self.reporter)

if __name__ == "__main__":
    unittest.main()

