def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError


    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)



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
    print(factorial_recursive(5))
    print(factorial_iterative(5))


if __name__ == '__main__':
    main()
