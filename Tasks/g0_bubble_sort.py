from random import randint
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for i in range(len(container) - 1):
        for j in range(len(container) - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]

    return container


def main():
    a = []
    for i in range(10):
        a.append(randint(1, 99))
    print(sort(a))


if __name__ == '__main__':
    main()