import unittest
from problems.problem_3 import three_sum

class TestProblem3(unittest.TestCase):
    def assertTripletsEqual(self, actual, expected):
        def normalize(triplets):
            if not isinstance(triplets, list):
                return triplets
            return sorted([sorted(list(t)) for t in triplets])
        self.assertEqual(normalize(actual), normalize(expected))

    def test_standard(self):
        self.assertTripletsEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_empty(self):
        self.assertTripletsEqual(three_sum([]), [])

    def test_one_element(self):
        self.assertTripletsEqual(three_sum([0]), [])

    def test_two_elements(self):
        self.assertTripletsEqual(three_sum([0, 1]), [])

    def test_three_elements_no_sum(self):
        self.assertTripletsEqual(three_sum([1, 2, 3]), [])

    def test_three_elements_match(self):
        self.assertTripletsEqual(three_sum([-1, 0, 1]), [[-1, 0, 1]])

    def test_all_zeroes(self):
        self.assertTripletsEqual(three_sum([0, 0, 0, 0]), [[0, 0, 0]])

    def test_multiple_triplets(self):
        self.assertTripletsEqual(three_sum([-2, 0, 1, 1, 2]), [[-2, 0, 2], [-2, 1, 1]])

    def test_only_positives(self):
        self.assertTripletsEqual(three_sum([1, 2, 3, 4, 5]), [])

    def test_only_negatives(self):
        self.assertTripletsEqual(three_sum([-1, -2, -3, -4]), [])

    def test_duplicate_triplets_prevention(self):
        self.assertTripletsEqual(three_sum([-1, 0, 1, -1, 0, 1]), [[-1, 0, 1]])

    def test_large_range(self):
        self.assertTripletsEqual(three_sum([-5, 2, 3, -4, 1, 3]), [[-5, 2, 3], [-4, 1, 3]])

    def test_no_combination(self):
        self.assertTripletsEqual(three_sum([-10, 5, 4, 3, 2]), [])

    def test_complex_duplicates(self):
        self.assertTripletsEqual(three_sum([-2, -2, 0, 2, 2, 0, 0]), [[-2, 0, 2], [0, 0, 0]])

    def test_five_elements_multiple(self):
        self.assertTripletsEqual(three_sum([-3, -1, 0, 1, 2, 4]), [[-3, 1, 2], [-1, 0, 1], [-3, -1, 4]])

if __name__ == "__main__":
    unittest.main()
