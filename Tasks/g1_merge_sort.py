from random import randint
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        mid = len(container) // 2
        left_list = container[:mid]
        right_list = container[mid:]

        sort(left_list)
        sort(right_list)

        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                container[k] = left_list[i]
                i = i + 1
            else:
                container[k] = right_list[j]
                j = j + 1
            k = k + 1

        while i < len(left_list):
            container[k] = left_list[i]
            i = i + 1
            k = k + 1

        while j < len(right_list):
            container[k] = right_list[j]
            j = j + 1
            k = k + 1
    return container


def main():
    a = [randint(1, 99) for i in range(10)]
    print(sort(a))


if __name__ == '__main__':
    main()
