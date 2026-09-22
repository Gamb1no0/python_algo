"""Проверка последовательностей добавления и удаления из стека."""


def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    """Проверить, можно ли получить popped при порядке добавления pushed."""
    if len(pushed) != len(popped):
        return False

    stack = []
    index = 0

    for number in pushed:
        stack.append(number)

        while stack and index < len(popped) and stack[-1] == popped[index]:
            stack.pop()
            index += 1

    return index == len(popped)


if __name__ == "__main__":
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    print(validate_stack_sequences(pushed, popped))
