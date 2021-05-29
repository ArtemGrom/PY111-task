def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return n

    n1 = 0
    n2 = 1

    for i in range(n - 1):
        n1, n2 = n2, n1 + n2
    return n2


def main():
    print(fib_iterative(5))


if __name__ == '__main__':
    main()

