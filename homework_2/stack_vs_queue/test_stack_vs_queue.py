"""Запуск из этой папки: python3 -m unittest -v."""

import unittest

from stack_vs_queue import Queue, Stack


class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(len(self.stack), 0)

    def test_empty_operations(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(len(self.stack), 0)

    def test_single_element(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.pop(), 10)
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(len(self.stack), 0)

    def test_last_in_first_out(self):
        for value in (1, 2, 3):
            self.stack.push(value)
        self.assertEqual(len(self.stack), 3)
        self.assertEqual([self.stack.pop() for _ in range(3)], [3, 2, 1])

    def test_peek_does_not_remove_element(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.peek(), 1)

    def test_mixed_operations(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.stack.push(30)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 30)
        self.assertEqual(self.stack.pop(), 10)
        self.assertTrue(self.stack.is_empty())

    def test_reuse_after_emptying(self):
        self.stack.push(1)
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.pop()
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(len(self.stack), 0)

    def test_repeated_negative_and_none_values(self):
        values = [0, -5, -5, None]
        for value in values:
            self.stack.push(value)
        self.assertEqual([self.stack.pop() for _ in values], [None, -5, -5, 0])
        self.assertTrue(self.stack.is_empty())

    def test_many_elements(self):
        for value in range(1000):
            self.stack.push(value)
        self.assertEqual(len(self.stack), 1000)
        for expected in range(999, -1, -1):
            self.assertEqual(self.stack.pop(), expected)
            self.assertEqual(len(self.stack), expected)
        self.assertTrue(self.stack.is_empty())


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_new_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_empty_operations(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.peek()
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_single_element(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_first_in_first_out(self):
        for value in (1, 2, 3):
            self.queue.enqueue(value)
        self.assertEqual(len(self.queue), 3)
        self.assertEqual([self.queue.dequeue() for _ in range(3)], [1, 2, 3])

    def test_peek_does_not_remove_element(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.peek(), 2)

    def test_mixed_operations(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.dequeue(), 10)
        self.queue.enqueue(30)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.dequeue(), 30)
        self.assertTrue(self.queue.is_empty())

    def test_reuse_after_emptying(self):
        self.queue.enqueue(1)
        self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 2)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_repeated_negative_and_none_values(self):
        values = [None, -5, -5, 0]
        for value in values:
            self.queue.enqueue(value)
        self.assertEqual([self.queue.dequeue() for _ in values], values)
        self.assertTrue(self.queue.is_empty())

    def test_many_elements(self):
        for value in range(1000):
            self.queue.enqueue(value)
        self.assertEqual(len(self.queue), 1000)
        for expected in range(1000):
            self.assertEqual(self.queue.dequeue(), expected)
            self.assertEqual(len(self.queue), 999 - expected)
        self.assertTrue(self.queue.is_empty())


if __name__ == "__main__":
    unittest.main()
