"""
Taylor series
"""
from typing import Union
import math


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    e = 0
    for i in range(0, 100):
        e = e + (x ** i) / math.factorial(i)
    return e


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sin_x = 0
    for i in range(0, 10):
        const = (-1) ** i
        sin_x = sin_x + ((x ** (2 * i + 1))/math.factorial(2 * i + 1)) * const
    return sin_x


def main():
    print(ex(10))
    print(sinx(10))


if __name__ == '__main__':
    main()


