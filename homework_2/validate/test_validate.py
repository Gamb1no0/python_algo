"""Запуск из этой папки: python3 -m unittest -v."""

import unittest

from validate import validate_stack_sequences


class ValidateTests(unittest.TestCase):
    def test_examples(self):
        self.assertIs(
            validate_stack_sequences([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]), True
        )
        self.assertIs(validate_stack_sequences([1, 2, 3], [3, 1, 2]), False)

    def test_single_element(self):
        self.assertIs(validate_stack_sequences([42], [42]), True)

    def test_same_order(self):
        self.assertIs(validate_stack_sequences([1, 2, 3], [1, 2, 3]), True)

    def test_reverse_order(self):
        self.assertIs(validate_stack_sequences([1, 2, 3], [3, 2, 1]), True)

    def test_other_valid_orders(self):
        pushed = [1, 2, 3, 4, 5]
        for popped in ([2, 1, 4, 3, 5], [3, 2, 1, 5, 4], [4, 5, 3, 2, 1]):
            with self.subTest(popped=popped):
                self.assertIs(validate_stack_sequences(pushed, popped), True)

    def test_invalid_orders(self):
        pushed = [1, 2, 3, 4, 5]
        for popped in ([3, 1, 2, 4, 5], [4, 3, 5, 1, 2], [5, 1, 2, 3, 4]):
            with self.subTest(popped=popped):
                self.assertIs(validate_stack_sequences(pushed, popped), False)

    def test_negative_zero_and_unsorted_numbers(self):
        pushed = [10, -2, 0, 7]
        self.assertIs(validate_stack_sequences(pushed, [-2, 7, 0, 10]), True)
        self.assertIs(validate_stack_sequences(pushed, [7, 10, 0, -2]), False)

    def test_inputs_are_not_changed(self):
        pushed = [1, 2, 3]
        for popped in ([2, 3, 1], [3, 1, 2]):
            with self.subTest(popped=popped):
                pushed_copy = pushed.copy()
                popped_copy = popped.copy()
                validate_stack_sequences(pushed, popped)
                self.assertEqual(pushed, pushed_copy)
                self.assertEqual(popped, popped_copy)

    def test_empty_sequences(self):
        self.assertIs(validate_stack_sequences([], []), True)

    def test_different_lengths(self):
        self.assertIs(validate_stack_sequences([1, 2], [1]), False)
        self.assertIs(validate_stack_sequences([1], [1, 2]), False)

    def test_maximum_size_same_order(self):
        pushed = list(range(100_000))
        self.assertIs(validate_stack_sequences(pushed, pushed.copy()), True)

    def test_maximum_size_reverse_order(self):
        pushed = list(range(100_000))
        self.assertIs(validate_stack_sequences(pushed, pushed[::-1]), True)

    def test_maximum_size_invalid_order(self):
        pushed = list(range(100_000))
        popped = [99_999] + list(range(99_999))
        self.assertIs(validate_stack_sequences(pushed, popped), False)


if __name__ == "__main__":
    unittest.main()
