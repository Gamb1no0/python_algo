"""Задача 1. BST: вставка и шесть обходов дерева."""

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node | None" = None
    right: "Node | None" = None


class BST:
    def __init__(self, values=()):
        self.root = None
        for value in values:
            self.insert(value)

    def insert(self, value):
        def add(node):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = add(node.left)
            elif value > node.value:
                node.right = add(node.right)
            # Повторные значения не добавляем.
            return node

        self.root = add(self.root)


def preorder(root):
    result = []

    def dfs(node):
        if node is None:
            return
        result.append(node.value)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def inorder(root):
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.value)
        dfs(node.right)

    dfs(root)
    return result


def postorder(root):
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.value)

    dfs(root)
    return result


def reverse_preorder(root):
    result = []

    def dfs(node):
        if node is None:
            return
        result.append(node.value)
        dfs(node.right)
        dfs(node.left)

    dfs(root)
    return result


def reverse_inorder(root):
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.right)
        result.append(node.value)
        dfs(node.left)

    dfs(root)
    return result


def reverse_postorder(root):
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.right)
        dfs(node.left)
        result.append(node.value)

    dfs(root)
    return result
