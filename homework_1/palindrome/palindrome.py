"""Проверка целого числа на палиндром без преобразования в строку."""


def is_palindrome(number: int) -> bool:
    """Вернуть True, если цифры числа одинаковы в обоих направлениях.

    Ожидается целое число. Ноль считается палиндромом,
    отрицательные числа — не палиндромами.
    """
    if number < 0:
        return False

    remaining = number
    reversed_number = 0

    while remaining > 0:
        digit = remaining % 10
        reversed_number = reversed_number * 10 + digit
        remaining //= 10

    return number == reversed_number


if __name__ == "__main__":
    print(is_palindrome(int(input())))
