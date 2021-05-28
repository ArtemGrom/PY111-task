"""
This module implements some functions based on linear search algo
"""
from typing import Sequence

arr = [3, 5, 2, 4, 7]


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_elem = arr[0]
    for ind, num in enumerate(arr):
        if num < min_elem:
            min_elem = ind
    return min_elem


if __name__ == '__main__':
    print(min_search(arr))
