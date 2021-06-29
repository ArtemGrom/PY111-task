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
    print(sort([63, 80, 62, 69, 71, 37, 12, 90, 19, 67]))


if __name__ == '__main__':
    main()