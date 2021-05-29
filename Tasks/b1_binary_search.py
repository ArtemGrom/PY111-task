from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    high = len(arr) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        find_elem = arr[mid]
        if elem > find_elem:
            low = mid + 1
        elif elem < find_elem:
            high = mid - 1
        else:
            while mid > 0 and arr[mid - 1] == elem:
                mid -= 1
            return mid

    return None


def main():
    # elem = 7
    # arr = [i for i in range(10)]
    print(binary_search(2, [2, 2, 2, 2, 2, 2, 2, 2]))


if __name__ == '__main__':
    main()
