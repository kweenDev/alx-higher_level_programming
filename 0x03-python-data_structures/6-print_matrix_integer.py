#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Args:
    - matrix: 2D list of integers to be printed.
    """
    for row in matrix:
        print(' '.join("{:d}".format(num) for num in row))


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
