import unittest
from problems.problem_10 import decode_string

class TestProblem10(unittest.TestCase):
    def test_standard_1(self):
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")

    def test_standard_2(self):
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")

    def test_standard_3(self):
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_empty(self):
        self.assertEqual(decode_string(""), "")

    def test_no_digits(self):
        self.assertEqual(decode_string("abc"), "abc")

    def test_single_char_repeated(self):
        self.assertEqual(decode_string("10[a]"), "aaaaaaaaaa")

    def test_multiple_nesting(self):
        self.assertEqual(decode_string("2[2[2[a]]]"), "aaaaaaaa")

    def test_nesting_with_surrounding(self):
        self.assertEqual(decode_string("a2[b3[c]d]e"), "abcccdbcccde")

    def test_large_repetition(self):
        self.assertEqual(decode_string("3[2[a]]"), "aaaaaa")

    def test_consecutive_nesting(self):
        self.assertEqual(decode_string("2[a]3[b2[c]]"), "aabccbccbcc")

    def test_single_letter_bracket(self):
        self.assertEqual(decode_string("1[a]"), "a")

    def test_complex_nesting(self):
        self.assertEqual(
            decode_string("3[z]2[2[y]pq4[2[jk]]]"),
            "zzzyypqjkjkjkjkjkjkjkyypqjkjkjkjkjkjkjkjk"
        )

    def test_bracket_around_everything(self):
        self.assertEqual(decode_string("2[3[a]]"), "aaaaaa")

    def test_long_expression(self):
        self.assertEqual(decode_string("abc3[cd]xyz"), "abccdcdcdxyz")

    def test_multi_digit_nesting(self):
        self.assertEqual(decode_string("12[ab]"), "abababababababababababab")

if __name__ == "__main__":
    unittest.main()
