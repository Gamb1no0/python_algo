"""Максимальная чётная сумма элементов массива."""


def max_even_sum(numbers: list[int]) -> int:
    """Найти максимальную чётную сумму для положительных целых чисел."""
    total = 0
    min_odd = None

    for number in numbers:
        total += number
        if number % 2 != 0:
            if min_odd is None or number < min_odd:
                min_odd = number

    if total % 2 == 0:
        return total

    # Если сумма нечётная, в массиве точно есть нечётное число.
    return total - min_odd


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(max_even_sum(numbers))
