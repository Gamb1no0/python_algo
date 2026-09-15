"""Запуск из этой папки: python3 -m unittest -v."""

import unittest

from palindrome import is_palindrome


class PalindromeTests(unittest.TestCase):
    def test_examples(self):
        self.assertIs(is_palindrome(121), True)
        self.assertIs(is_palindrome(31), False)

    def test_single_digits_and_zero(self):
        for number in range(10):
            with self.subTest(number=number):
                self.assertIs(is_palindrome(number), True)

    def test_palindromes(self):
        for number in (11, 1221, 12321, 1001, 10001, 12021, 123454321):
            with self.subTest(number=number):
                self.assertIs(is_palindrome(number), True)

    def test_non_palindromes(self):
        for number in (12, 123, 1231, 123421, 1002, 12031):
            with self.subTest(number=number):
                self.assertIs(is_palindrome(number), False)

    def test_trailing_zeros(self):
        for number in (10, 100, 1010, 12210):
            with self.subTest(number=number):
                self.assertIs(is_palindrome(number), False)

    def test_negative_numbers(self):
        for number in (-1, -121, -1221):
            with self.subTest(number=number):
                self.assertIs(is_palindrome(number), False)

    def test_large_integers(self):
        self.assertIs(is_palindrome(10**100 + 1), True)
        self.assertIs(is_palindrome(10**100 + 2), False)


if __name__ == "__main__":
    unittest.main()
