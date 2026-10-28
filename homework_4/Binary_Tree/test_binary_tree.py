"""Тесты всех трёх задач. Запуск: python -m unittest -v"""

import unittest

from task_1 import (
    BST, Node, preorder, inorder, postorder,
    reverse_preorder, reverse_inorder, reverse_postorder,
)
from task_2 import is_valid_bst
from task_3 import is_balanced

TRAVERSALS = (
    preorder, inorder, postorder,
    reverse_preorder, reverse_inorder, reverse_postorder,
)


class TestTraversal(unittest.TestCase):
    def test_all_six_traversals(self):
        root = BST([8, 3, 10, 1, 6, 14, 4, 7, 13]).root
        expected = {
            preorder: [8, 3, 1, 6, 4, 7, 10, 14, 13],
            inorder: [1, 3, 4, 6, 7, 8, 10, 13, 14],
            postorder: [1, 4, 7, 6, 3, 13, 14, 10, 8],
            reverse_preorder: [8, 10, 14, 13, 3, 6, 7, 4, 1],
            reverse_inorder: [14, 13, 10, 8, 7, 6, 4, 3, 1],
            reverse_postorder: [13, 14, 10, 7, 4, 6, 1, 3, 8],
        }
        for traversal, result in expected.items():
            with self.subTest(traversal=traversal.__name__):
                self.assertEqual(traversal(root), result)

    def test_empty_tree(self):
        for traversal in TRAVERSALS:
            self.assertEqual(traversal(None), [])

    def test_one_node(self):
        for traversal in TRAVERSALS:
            self.assertEqual(traversal(Node(42)), [42])

    def test_duplicate_insertion(self):
        tree = BST([5, 3, 7, 3, 5, 7])
        self.assertEqual(inorder(tree.root), [3, 5, 7])

    def test_increasing_insertion(self):
        tree = BST([1, 2, 3, 4])
        self.assertEqual(inorder(tree.root), [1, 2, 3, 4])
        self.assertEqual(postorder(tree.root), [4, 3, 2, 1])

    def test_decreasing_insertion(self):
        tree = BST([4, 3, 2, 1])
        self.assertEqual(inorder(tree.root), [1, 2, 3, 4])
        self.assertEqual(preorder(tree.root), [4, 3, 2, 1])

    def test_negative_keys(self):
        tree = BST([0, -2, 5, -10])
        self.assertEqual(inorder(tree.root), [-10, -2, 0, 5])


class TestValidateBST(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_valid_bst(None))

    def test_one_node(self):
        self.assertTrue(is_valid_bst(Node(7)))

    def test_valid_bst(self):
        self.assertTrue(is_valid_bst(BST([8, 3, 10, 1, 6, 14, 4]).root))

    def test_invalid_child(self):
        self.assertFalse(is_valid_bst(Node(10, Node(12), Node(15))))

    def test_invalid_deep_right_subtree(self):
        root = Node(10, Node(5), Node(15, Node(6), Node(20)))
        self.assertFalse(is_valid_bst(root))

    def test_invalid_deep_left_subtree(self):
        root = Node(10, Node(5, None, Node(12)), Node(15))
        self.assertFalse(is_valid_bst(root))

    def test_duplicate_keys(self):
        self.assertFalse(is_valid_bst(Node(5, Node(5))))
        self.assertFalse(is_valid_bst(Node(5, None, Node(5))))

    def test_negative_keys(self):
        self.assertTrue(is_valid_bst(Node(0, Node(-5), Node(5))))


class TestBalanced(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_balanced(None))

    def test_one_node(self):
        self.assertTrue(is_balanced(Node(5)))

    def test_perfect_tree(self):
        root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
        self.assertTrue(is_balanced(root))

    def test_height_difference_one(self):
        root = Node(2, Node(1), Node(4, Node(3)))
        self.assertTrue(is_balanced(root))

    def test_long_chain(self):
        self.assertFalse(is_balanced(Node(1, None, Node(2, None, Node(3)))))

    def test_unbalanced_descendant(self):
        # У корня обе высоты равны 2, но узел 10 не сбалансирован.
        root = Node(
            8,
            Node(3, Node(1), Node(6, Node(4), Node(7))),
            Node(10, None, Node(14, Node(13))),
        )
        self.assertFalse(is_balanced(root))

    def test_need_not_be_bst(self):
        self.assertTrue(is_balanced(Node(1, Node(100), Node(-100))))


if __name__ == "__main__":
    unittest.main()
