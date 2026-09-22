"""Запуск из этой папки: python3 -m unittest -v."""

import unittest

from merge_lists import ListNode, merge_with_dummy, merge_without_dummy


def make_list(values):
    nodes = [ListNode(value) for value in values]
    for index in range(len(nodes) - 1):
        nodes[index].next = nodes[index + 1]
    head = nodes[0] if nodes else None
    return head, nodes


class MergeListsTests(unittest.TestCase):
    def check_merge(self, values1, values2, expected):
        for merge in (merge_with_dummy, merge_without_dummy):
            with self.subTest(method=merge.__name__):
                list1, nodes1 = make_list(values1)
                list2, nodes2 = make_list(values2)
                original_nodes = nodes1 + nodes2
                original_values = [node.val for node in original_nodes]

                current = merge(list1, list2)
                result_values = []
                result_ids = []
                seen = set()

                while current is not None:
                    node_id = id(current)
                    self.assertNotIn(node_id, seen, "В результате появился цикл")
                    seen.add(node_id)
                    result_ids.append(node_id)
                    result_values.append(current.val)
                    current = current.next

                self.assertEqual(result_values, expected)
                # Проверяем, что использованы именно исходные узлы и все по разу.
                self.assertCountEqual(result_ids, [id(node) for node in original_nodes])
                self.assertEqual([node.val for node in original_nodes], original_values)

    def test_example(self):
        self.check_merge([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_both_empty(self):
        self.check_merge([], [], [])

    def test_first_empty(self):
        self.check_merge([], [1, 2, 3], [1, 2, 3])

    def test_second_empty(self):
        self.check_merge([1, 2, 3], [], [1, 2, 3])

    def test_single_elements(self):
        self.check_merge([1], [2], [1, 2])
        self.check_merge([2], [1], [1, 2])
        self.check_merge([1], [1], [1, 1])

    def test_interleaved_values(self):
        self.check_merge([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6])

    def test_first_list_before_second(self):
        self.check_merge([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])

    def test_second_list_before_first(self):
        self.check_merge([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6])

    def test_different_lengths(self):
        self.check_merge([3], [1, 2, 4, 5, 6], [1, 2, 3, 4, 5, 6])
        self.check_merge([1, 2, 4, 5, 6], [3], [1, 2, 3, 4, 5, 6])

    def test_repeated_values(self):
        self.check_merge([2, 2], [2, 2, 2], [2, 2, 2, 2, 2])
        self.check_merge([1, 1, 3], [1, 2, 3, 3], [1, 1, 1, 2, 3, 3, 3])

    def test_negative_values_and_zero(self):
        self.check_merge([-5, -1, 0], [-4, -1, 2], [-5, -4, -1, -1, 0, 2])

    def test_long_lists(self):
        self.check_merge(
            list(range(0, 10_000, 2)),
            list(range(1, 10_000, 2)),
            list(range(10_000)),
        )


if __name__ == "__main__":
    unittest.main()
