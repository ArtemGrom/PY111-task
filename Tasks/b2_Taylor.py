"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    e = 0
    a = x ** 1
    b = factorial_iterative(1)
    for i in range(2, 100):
        e += a / b
        a *= x
        b *= i
    return e + 1


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sin_x = 0
    for i in range(0, 10):
        const = (-1) ** i
        sin_x += ((x ** (2 * i + 1))/factorial_iterative(2 * i + 1)) * const
    return sin_x


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError

    n1 = 1
    while n > 1:
        n1 = n1 * n
        n -= 1

    return n1


def main():
    print(ex(10))
    print(sinx(10))


if __name__ == '__main__':
    main()


