import unittest
from problems.problem_7 import subarray_sum

class TestProblem7(unittest.TestCase):
    def test_standard_1(self):
        self.assertEqual(subarray_sum([1, 1, 1], 2), 2)

    def test_standard_2(self):
        self.assertEqual(subarray_sum([1, 2, 3], 3), 2)

    def test_empty(self):
        self.assertEqual(subarray_sum([], 5), 0)

    def test_single_match(self):
        self.assertEqual(subarray_sum([5], 5), 1)

    def test_single_no_match(self):
        self.assertEqual(subarray_sum([3], 5), 0)

    def test_all_zeroes_k_zero(self):
        self.assertEqual(subarray_sum([0, 0, 0], 0), 6)

    def test_negatives_zero_sum(self):
        self.assertEqual(subarray_sum([-1, 1, -1, 1], 0), 4)

    def test_negatives_positive_k(self):
        self.assertEqual(subarray_sum([-1, -1, 2, 1], 2), 2)

    def test_k_not_found(self):
        self.assertEqual(subarray_sum([1, 2, 3], 10), 0)

    def test_entire_array(self):
        self.assertEqual(subarray_sum([1, 2, 3], 6), 1)

    def test_all_positives_large_k(self):
        self.assertEqual(subarray_sum([10, 2, -2, -20, 10], -10), 3)

    def test_alternating(self):
        self.assertEqual(subarray_sum([1, -1, 1, -1], 1), 4)

    def test_large_elements(self):
        self.assertEqual(subarray_sum([1000000, -1000000, 5], 5), 2)

    def test_single_negative(self):
        self.assertEqual(subarray_sum([-5], -5), 1)

    def test_multiple_sums(self):
        self.assertEqual(subarray_sum([9, 4, 20, 3, 10, 5], 33), 2)

if __name__ == "__main__":
    unittest.main()
