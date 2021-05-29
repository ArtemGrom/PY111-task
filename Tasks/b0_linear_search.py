"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import random


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_elem = arr[0]
    min_elem_ind = 0
    for ind, num in enumerate(arr):
        if num < min_elem:
            min_elem = num
            min_elem_ind = ind
    return min_elem_ind


if __name__ == '__main__':
    arr = [random.randint(-100, 100) for _ in range(300)]
    print(arr)
    print(min_search(arr))
