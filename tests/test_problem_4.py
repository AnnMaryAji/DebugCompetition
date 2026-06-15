import unittest
from problems.problem_4 import group_anagrams

class TestProblem4(unittest.TestCase):
    def assertGroupsEqual(self, actual, expected):
        def normalize(groups):
            if not isinstance(groups, list):
                return groups
            return sorted([sorted(list(g)) for g in groups])
        self.assertEqual(normalize(actual), normalize(expected))

    def test_standard(self):
        self.assertGroupsEqual(
            group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        )

    def test_empty_list(self):
        self.assertGroupsEqual(group_anagrams([]), [])

    def test_single_empty_string(self):
        self.assertGroupsEqual(group_anagrams([""]), [[""]])

    def test_single_char(self):
        self.assertGroupsEqual(group_anagrams(["a"]), [["a"]])

    def test_all_anagrams(self):
        self.assertGroupsEqual(
            group_anagrams(["abc", "bca", "cab", "acb"]),
            [["abc", "bca", "cab", "acb"]]
        )

    def test_all_unique(self):
        self.assertGroupsEqual(
            group_anagrams(["abc", "def", "ghi"]),
            [["abc"], ["def"], ["ghi"]]
        )

    def test_duplicate_words(self):
        self.assertGroupsEqual(
            group_anagrams(["dog", "dog", "god"]),
            [["dog", "dog", "god"]]
        )

    def test_case_sensitivity(self):
        self.assertGroupsEqual(
            group_anagrams(["eat", "Tea"]),
            [["eat"], ["Tea"]]
        )

    def test_mixed_lengths(self):
        self.assertGroupsEqual(
            group_anagrams(["a", "ab", "ba", "abc", "bca"]),
            [["a"], ["ab", "ba"], ["abc", "bca"]]
        )

    def test_numbers_in_strings(self):
        self.assertGroupsEqual(
            group_anagrams(["123", "321", "132", "456"]),
            [["123", "321", "132"], ["456"]]
        )

    def test_special_chars(self):
        self.assertGroupsEqual(
            group_anagrams(["a#b", "b#a", "ab#"]),
            [["a#b", "b#a"], ["ab#"]]
        )

    def test_long_words(self):
        self.assertGroupsEqual(
            group_anagrams(["anagram", "nagaram", "gate", "teag"]),
            [["anagram", "nagaram"], ["gate", "teag"]]
        )

    def test_repeating_letters(self):
        self.assertGroupsEqual(
            group_anagrams(["aab", "aba", "baa", "abb"]),
            [["aab", "aba", "baa"], ["abb"]]
        )

    def test_empty_and_space(self):
        self.assertGroupsEqual(group_anagrams(["", " "]), [[""], [" "]])

    def test_many_singles(self):
        self.assertGroupsEqual(
            group_anagrams(["a", "b", "c", "d"]),
            [["a"], ["b"], ["c"], ["d"]]
        )

if __name__ == "__main__":
    unittest.main()
