"""Поиск двух индексов, сумма элементов на которых равна k."""


def two_sum(arr: list[int], k: int) -> tuple[int, int]:
    """Вернуть индексы пары по возрастанию. Если пары нет — ValueError."""
    seen = {}

    for index, number in enumerate(arr):
        needed = k - number
        if needed in seen:
            return seen[needed], index
        seen[number] = index

    raise ValueError("Подходящей пары нет")


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    first, second = two_sum(arr, k)
    print(first, second)
