import unittest
from problems.problem_6 import product_except_self

class TestProblem6(unittest.TestCase):
    def test_standard_1(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_standard_2(self):
        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_two_elements(self):
        self.assertEqual(product_except_self([2, 3]), [3, 2])

    def test_all_ones(self):
        self.assertEqual(product_except_self([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_all_neg_ones(self):
        self.assertEqual(product_except_self([-1, -1, -1, -1]), [-1, -1, -1, -1])

    def test_with_two_zeroes(self):
        self.assertEqual(product_except_self([1, 2, 0, 4, 0]), [0, 0, 0, 0, 0])

    def test_single_zero(self):
        self.assertEqual(product_except_self([1, 2, 0, 4]), [0, 0, 8, 0])

    def test_alternating_negatives(self):
        self.assertEqual(product_except_self([1, -2, 3, -4]), [24, -12, 8, -6])

    def test_large_numbers(self):
        self.assertEqual(product_except_self([10, 20, 30]), [600, 300, 200])

    def test_zeros_and_negatives(self):
        self.assertEqual(product_except_self([-1, 0, -2, 0]), [0, 0, 0, 0])

    def test_three_elements(self):
        self.assertEqual(product_except_self([1, 5, 10]), [50, 10, 5])

    def test_large_values(self):
        self.assertEqual(product_except_self([5, 2, 1]), [2, 5, 10])

    def test_repeated_elements(self):
        self.assertEqual(product_except_self([2, 2, 2]), [4, 4, 4])

    def test_long_ascending(self):
        self.assertEqual(product_except_self([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

    def test_increasing_negatives(self):
        self.assertEqual(product_except_self([-1, -2, -3]), [6, 3, 2])

if __name__ == "__main__":
    unittest.main()
