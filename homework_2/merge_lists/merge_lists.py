"""Два способа слияния отсортированных односвязных списков."""


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def merge_with_dummy(list1, list2):
    """Объединить исходные узлы с помощью фиктивного начального узла."""
    dummy = ListNode(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return dummy.next


def merge_without_dummy(list1, list2):
    """Объединить исходные узлы без создания фиктивного узла."""
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    tail = head

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return head


if __name__ == "__main__":
    for title, merge in (
        ("С фиктивным узлом", merge_with_dummy),
        ("Без фиктивного узла", merge_without_dummy),
    ):
        # Для каждого способа создаём отдельные списки: слияние меняет связи.
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        head = merge(list1, list2)

        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        print(title + ":", values)
