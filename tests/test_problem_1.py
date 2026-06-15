import unittest
from problems.problem_1 import longest_substring

class TestProblem1(unittest.TestCase):
    def test_standard_1(self):
        self.assertEqual(longest_substring("abcabcbb"), 3)

    def test_standard_2(self):
        self.assertEqual(longest_substring("pwwkew"), 3)

    def test_all_same(self):
        self.assertEqual(longest_substring("bbbbbb"), 1)

    def test_empty(self):
        self.assertEqual(longest_substring(""), 0)

    def test_single_char(self):
        self.assertEqual(longest_substring("a"), 1)

    def test_two_chars_different(self):
        self.assertEqual(longest_substring("ab"), 2)

    def test_two_chars_same(self):
        self.assertEqual(longest_substring("aa"), 1)

    def test_all_unique(self):
        self.assertEqual(longest_substring("abcdefg"), 7)

    def test_numbers(self):
        self.assertEqual(longest_substring("123412356"), 6)

    def test_special_characters(self):
        self.assertEqual(longest_substring("a!@#a$%^&*"), 8)

    def test_spaces(self):
        self.assertEqual(longest_substring("abc d e"), 5)

    def test_alternating(self):
        self.assertEqual(longest_substring("abababab"), 2)

    def test_long_string(self):
        self.assertEqual(longest_substring("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_repeated_at_ends(self):
        self.assertEqual(longest_substring("abca"), 3)

    def test_duplicate_in_middle(self):
        self.assertEqual(longest_substring("abcbde"), 4)

if __name__ == "__main__":
    unittest.main()
