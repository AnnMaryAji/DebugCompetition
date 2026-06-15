import unittest
from problems.problem_5 import longest_consecutive

class TestProblem5(unittest.TestCase):
    def test_standard_1(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_standard_2(self):
        self.assertEqual(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_empty(self):
        self.assertEqual(longest_consecutive([]), 0)

    def test_single(self):
        self.assertEqual(longest_consecutive([10]), 1)

    def test_all_same(self):
        self.assertEqual(longest_consecutive([5, 5, 5, 5]), 1)

    def test_negative(self):
        self.assertEqual(longest_consecutive([-3, -2, -1, 0, 1]), 5)

    def test_mixed_negatives(self):
        self.assertEqual(longest_consecutive([-5, 2, 4, -4, -3, 1, 3]), 4)

    def test_no_consecutive(self):
        self.assertEqual(longest_consecutive([2, 4, 6, 8, 10]), 1)

    def test_consecutive_descending(self):
        self.assertEqual(longest_consecutive([5, 4, 3, 2, 1]), 5)

    def test_consecutive_ascending(self):
        self.assertEqual(longest_consecutive([1, 2, 3, 4, 5]), 5)

    def test_multiple_sequences_same_len(self):
        self.assertEqual(longest_consecutive([1, 2, 10, 11]), 2)

    def test_large_gap(self):
        self.assertEqual(longest_consecutive([1, 1000000]), 1)

    def test_duplicates_inside(self):
        self.assertEqual(longest_consecutive([1, 2, 2, 3, 4, 4]), 4)

    def test_zero_and_negatives(self):
        self.assertEqual(longest_consecutive([-1, 0, -2]), 3)

    def test_large_sequence(self):
        self.assertEqual(longest_consecutive(list(range(100))), 100)

if __name__ == "__main__":
    unittest.main()
