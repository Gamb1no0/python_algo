"""Запуск из этой папки: python3 -m unittest -v."""

import unittest

from prime import count_primes


class CountPrimesTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_primes(10), 4)
        self.assertEqual(count_primes(1), 0)

    def test_numbers_below_two(self):
        for n in (-10, -1, 0, 1):
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), 0)

    def test_two_is_not_included(self):
        self.assertEqual(count_primes(2), 0)

    def test_small_numbers(self):
        for n, expected in ((3, 1), (4, 2), (5, 2), (6, 3), (8, 4), (9, 4)):
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), expected)

    def test_prime_upper_bound(self):
        for n, expected in ((7, 3), (11, 4), (13, 5), (17, 6), (19, 7)):
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), expected)
                self.assertEqual(count_primes(n + 1), expected + 1)

    def test_prime_squares(self):
        for n, expected in ((9, 4), (25, 9), (49, 15), (121, 30)):
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), expected)
                self.assertEqual(count_primes(n + 1), expected)

    def test_larger_numbers(self):
        for n, expected in ((20, 8), (100, 25), (1000, 168), (10000, 1229)):
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), expected)

    def test_against_simple_divisor_check(self):
        # Для маленьких N сравниваем решето с обычным перебором делителей.
        for n in range(101):
            expected = 0
            for number in range(2, n):
                if all(number % divisor != 0 for divisor in range(2, number)):
                    expected += 1
            with self.subTest(n=n):
                self.assertEqual(count_primes(n), expected)


if __name__ == "__main__":
    unittest.main()
