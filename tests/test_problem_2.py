import unittest
from problems.problem_2 import max_area

class TestProblem2(unittest.TestCase):
    def test_standard_1(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_two_elements_same(self):
        self.assertEqual(max_area([1, 1]), 1)

    def test_two_elements_diff(self):
        self.assertEqual(max_area([1, 2]), 1)

    def test_increasing(self):
        self.assertEqual(max_area([1, 2, 3, 4, 5]), 6)

    def test_decreasing(self):
        self.assertEqual(max_area([5, 4, 3, 2, 1]), 6)

    def test_flat(self):
        self.assertEqual(max_area([4, 4, 4, 4, 4]), 16)

    def test_valley(self):
        self.assertEqual(max_area([5, 1, 1, 5]), 15)

    def test_peak(self):
        self.assertEqual(max_area([1, 5, 5, 1]), 5)

    def test_large_difference(self):
        self.assertEqual(max_area([10, 1, 1, 10]), 30)

    def test_single_huge_middle(self):
        self.assertEqual(max_area([1, 2, 10, 2, 1]), 4)

    def test_alternating(self):
        self.assertEqual(max_area([2, 3, 2, 3, 2]), 8)

    def test_empty_heights(self):
        self.assertEqual(max_area([]), 0)

    def test_one_height(self):
        self.assertEqual(max_area([5]), 0)

    def test_zero_heights(self):
        self.assertEqual(max_area([0, 0, 0]), 0)

    def test_large_list(self):
        self.assertEqual(max_area([1, 100, 100, 1]), 100)

if __name__ == "__main__":
    unittest.main()
