#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """
    Computes the square value of all integers in a matrix using map.

    :param matrix: A 2-dimensional array.
    :return: A new matrix with each value being the square of the input.
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
