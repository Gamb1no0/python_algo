"""Запуск из этой папки: python3 -m unittest -v."""

import unittest

from sum import max_even_sum


class MaxEvenSumTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_even_sum([5, 7, 13, 2, 14]), 36)
        self.assertEqual(max_even_sum([3]), 0)

    def test_empty_array(self):
        self.assertEqual(max_even_sum([]), 0)

    def test_single_number(self):
        for numbers, expected in (([1], 0), ([9], 0), ([2], 2), ([100], 100)):
            with self.subTest(numbers=numbers):
                self.assertEqual(max_even_sum(numbers), expected)

    def test_only_even_numbers(self):
        self.assertEqual(max_even_sum([2, 4, 6, 8]), 20)

    def test_only_odd_numbers(self):
        for numbers, expected in (([5, 7], 12), ([1, 3, 5], 8), ([3, 5, 7, 9], 24)):
            with self.subTest(numbers=numbers):
                self.assertEqual(max_even_sum(numbers), expected)

    def test_mixed_numbers_with_even_total(self):
        self.assertEqual(max_even_sum([1, 2, 3, 4]), 10)

    def test_remove_smallest_odd_not_smallest_number(self):
        self.assertEqual(max_even_sum([2, 9, 7, 5]), 18)

    def test_minimum_odd_at_different_positions(self):
        for numbers in ([3, 9, 7], [9, 3, 7], [9, 7, 3]):
            with self.subTest(numbers=numbers):
                self.assertEqual(max_even_sum(numbers), 16)

    def test_repeated_numbers(self):
        for numbers, expected in (([3, 3, 3], 6), ([1, 1], 2), ([2, 2, 2], 6)):
            with self.subTest(numbers=numbers):
                self.assertEqual(max_even_sum(numbers), expected)

    def test_large_numbers(self):
        self.assertEqual(max_even_sum([10**20, 10**20 + 1, 3]), 2 * 10**20 + 4)
        self.assertEqual(max_even_sum([10**20, 10**20 + 1]), 10**20)


if __name__ == "__main__":
    unittest.main()
