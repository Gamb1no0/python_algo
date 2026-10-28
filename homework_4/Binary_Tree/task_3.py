"""Задача 3. Проверка сбалансированности бинарного дерева."""


def is_balanced(root):
    def check(node):
        # Возвращает (высота, сбалансировано ли поддерево).
        if node is None:
            return -1, True

        left_height, left_ok = check(node.left)
        right_height, right_ok = check(node.right)

        height = 1 + max(left_height, right_height)
        balanced = (left_ok and right_ok
                    and abs(left_height - right_height) <= 1)
        return height, balanced

    return check(root)[1]
