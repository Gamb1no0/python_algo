"""Стек и очередь на односвязных списках."""


class _Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        self._top = _Node(value, self._top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")

        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._top.value

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value):
        node = _Node(value)
        if self.is_empty():
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")

        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size


if __name__ == "__main__":
    stack = Stack()
    queue = Queue()

    for number in (1, 2, 3):
        stack.push(number)
        queue.enqueue(number)

    print("Стек:", stack.pop(), stack.pop(), stack.pop())
    print("Очередь:", queue.dequeue(), queue.dequeue(), queue.dequeue())
