"""Задача 2. Проверка корректности бинарного дерева поиска."""


def is_valid_bst(root):
    def check(node, low, high):
        if node is None:
            return True

        if low is not None and node.value <= low:
            return False
        if high is not None and node.value >= high:
            return False

        return (check(node.left, low, node.value)
                and check(node.right, node.value, high))

    return check(root, None, None)
