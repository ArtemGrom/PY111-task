from random import randint
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container
    else:
        sup_elem = container[0]
        less = [x for x in container[1:] if x < sup_elem]
        greater = [x for x in container[1:] if x >= sup_elem]

        return sort(less) + [sup_elem] + sort(greater)


def main():
    a = []
    for i in range(10):
        a.append(randint(1, 99))
    print(sort(a))


if __name__ == '__main__':
    main()
