"""Запуск из этой папки: python3 -m unittest -v."""

from pathlib import Path
import subprocess
import sys
import unittest

from two_sum import two_sum


class TwoSumTests(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(two_sum([1, 3, 4, 10], 7), (1, 2))

    def test_second_example(self):
        self.assertEqual(two_sum([5, 5, 1, 4], 10), (0, 1))

    def test_two_elements(self):
        self.assertEqual(two_sum([9, 2], 11), (0, 1))

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-8, -3, -6, -2], -9), (1, 2))

    def test_zero_target(self):
        self.assertEqual(two_sum([7, -4, 0, 4], 0), (1, 3))

    def test_pair_with_zero(self):
        self.assertEqual(two_sum([0, 9, 3, 5], 5), (0, 3))

    def test_two_zeros(self):
        self.assertEqual(two_sum([0, 8, 0], 0), (0, 2))

    def test_first_and_last_elements(self):
        self.assertEqual(two_sum([12, 1, 2, 3, -5], 7), (0, 4))

    def test_same_element_cannot_be_used_twice(self):
        self.assertEqual(two_sum([3, 2, 4], 6), (1, 2))

    def test_large_integers(self):
        big = 10**30
        self.assertEqual(two_sum([big, 4, -big + 7], 7), (0, 2))

    def test_input_is_not_changed(self):
        arr = [8, 2, 11, 7, 4]
        original = arr.copy()
        self.assertEqual(two_sum(arr, 9), (1, 3))
        self.assertEqual(arr, original)

    def test_large_array(self):
        arr = list(range(100_000))
        self.assertEqual(two_sum(arr, 199_997), (99_998, 99_999))

    def test_no_pair(self):
        for arr, k in (([], 0), ([3], 6), ([1, 2, 5], 20)):
            with self.subTest(arr=arr, k=k):
                with self.assertRaises(ValueError):
                    two_sum(arr, k)

    def test_console_examples(self):
        script = Path(__file__).with_name("two_sum.py")
        for data, expected in (("1 3 4 10\n7\n", "1 2\n"),
                               ("5 5 1 4\n10\n", "0 1\n")):
            with self.subTest(data=data):
                result = subprocess.run(
                    [sys.executable, str(script)],
                    input=data, text=True, capture_output=True, check=True,
                )
                self.assertEqual(result.stdout, expected)


if __name__ == "__main__":
    unittest.main()
