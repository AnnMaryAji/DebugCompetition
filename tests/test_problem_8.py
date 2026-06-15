import unittest
from problems.problem_8 import merge_intervals

class TestProblem8(unittest.TestCase):
    def assertIntervalsEqual(self, actual, expected):
        def normalize(ints):
            if not isinstance(ints, list):
                return ints
            return sorted([list(i) for i in ints])
        self.assertEqual(normalize(actual), normalize(expected))

    def test_standard_1(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]]
        )

    def test_standard_2(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 4], [4, 5]]),
            [[1, 5]]
        )

    def test_empty(self):
        self.assertIntervalsEqual(merge_intervals([]), [])

    def test_single(self):
        self.assertIntervalsEqual(merge_intervals([[1, 5]]), [[1, 5]])

    def test_no_overlaps(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 2], [3, 4], [5, 6]]),
            [[1, 2], [3, 4], [5, 6]]
        )

    def test_all_overlapping(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 5], [2, 6], [3, 7], [4, 8]]),
            [[1, 8]]
        )

    def test_nested_intervals(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 10], [2, 5], [6, 8]]),
            [[1, 10]]
        )

    def test_unsorted_input(self):
        self.assertIntervalsEqual(
            merge_intervals([[15, 18], [8, 10], [2, 6], [1, 3]]),
            [[1, 6], [8, 10], [15, 18]]
        )

    def test_adjacent_points(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 4], [0, 0]]),
            [[0, 0], [1, 4]]
        )

    def test_equal_intervals(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 3], [1, 3], [1, 3]]),
            [[1, 3]]
        )

    def test_single_point_intervals(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 1], [1, 2], [2, 2]]),
            [[1, 2]]
        )

    def test_overlapping_point(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 2], [2, 3], [3, 4]]),
            [[1, 4]]
        )

    def test_nested_reversed(self):
        self.assertIntervalsEqual(
            merge_intervals([[2, 3], [1, 4]]),
            [[1, 4]]
        )

    def test_disjoint_with_gaps(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 2], [4, 5], [7, 8]]),
            [[1, 2], [4, 5], [7, 8]]
        )

    def test_huge_interval_at_start(self):
        self.assertIntervalsEqual(
            merge_intervals([[1, 100], [2, 3], [4, 5], [99, 101]]),
            [[1, 101]]
        )

if __name__ == "__main__":
    unittest.main()
