"""Количество простых чисел строго меньше N."""


def count_primes(n: int) -> int:
    """Посчитать простые числа меньше n с помощью решета Эратосфена."""
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    number = 2
    while number * number < n:
        if is_prime[number]:
            for multiple in range(number * number, n, number):
                is_prime[multiple] = False
        number += 1

    return sum(is_prime)


if __name__ == "__main__":
    print(count_primes(int(input())))
