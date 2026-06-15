import unittest
from problems.problem_9 import find_anagrams

class TestProblem9(unittest.TestCase):
    def assertIndicesEqual(self, actual, expected):
        self.assertEqual(sorted(actual), sorted(expected))

    def test_standard_1(self):
        self.assertIndicesEqual(find_anagrams("cbaebabacd", "abc"), [0, 6])

    def test_standard_2(self):
        self.assertIndicesEqual(find_anagrams("abab", "ab"), [0, 1, 2])

    def test_empty_s(self):
        self.assertIndicesEqual(find_anagrams("", "a"), [])

    def test_empty_p(self):
        self.assertIndicesEqual(find_anagrams("abc", ""), [])

    def test_p_longer_than_s(self):
        self.assertIndicesEqual(find_anagrams("ab", "abc"), [])

    def test_exact_match(self):
        self.assertIndicesEqual(find_anagrams("abc", "abc"), [0])

    def test_no_anagrams(self):
        self.assertIndicesEqual(find_anagrams("cbaebabacd", "xyz"), [])

    def test_all_same_chars(self):
        self.assertIndicesEqual(find_anagrams("aaaaa", "aa"), [0, 1, 2, 3])

    def test_overlapping_anagrams(self):
        self.assertIndicesEqual(find_anagrams("aaaa", "aaa"), [0, 1])

    def test_single_char(self):
        self.assertIndicesEqual(find_anagrams("a", "a"), [0])

    def test_single_char_no_match(self):
        self.assertIndicesEqual(find_anagrams("a", "b"), [])

    def test_disjoint(self):
        self.assertIndicesEqual(find_anagrams("abcd", "cd"), [2])

    def test_repeated_disjoint(self):
        self.assertIndicesEqual(find_anagrams("abacaba", "ab"), [0, 1, 4, 5])

    def test_caps_no_match(self):
        self.assertIndicesEqual(find_anagrams("abc", "ABC"), [])

    def test_long_gap(self):
        self.assertIndicesEqual(find_anagrams("a" + "b" * 10 + "a", "a"), [0, 11])

if __name__ == "__main__":
    unittest.main()
