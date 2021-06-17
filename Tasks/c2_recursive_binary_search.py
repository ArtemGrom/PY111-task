from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, low=0, high=None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if high is None:
        high = len(arr) - 1
    if low > high:
        return None
    mid = (high + low) // 2
    if arr[mid] == elem:
        while mid > 0 and arr[mid - 1] == elem:
            mid -= 1
        return mid
    elif elem < arr[mid]:
        return binary_search(elem, arr, low, mid - 1)
    else:
        return binary_search(elem, arr, mid + 1, high)


def main():
    elem = 98
    arr = [190, 8, 17, 45, 69, 98, 122, 185]
    print(binary_search(elem, arr, 0, len(arr)-1))


if __name__ == '__main__':
    main()


