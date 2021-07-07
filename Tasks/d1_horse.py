def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    n, m = shape
    field = [[0] * m for _ in range(n)]
    field[0][0] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] != 0:
                if 0 <= i + 1 < n and 0 <= j + 2 < m:
                    field[i + 1][j + 2] += 2 * field[i][j]
                if 0 <= i + 2 < n and 0 <= j + 1 < m:
                    field[i + 2][j + 1] += 2 * field[i][j]
                if 0 <= i + 1 < n and 0 <= j - 2 < m:
                    field[i + 1][j - 2] += 2 * field[i][j]
                if 0 <= i + 2 < n and 0 <= j - 1 < m:
                    field[i + 2][j - 1] += 2 * field[i][j]

    return field[point[0]][point[1]]


def main():
    print(calculate_paths((8, 8), (7, 7)))


if __name__ == '__main__':
    main()
