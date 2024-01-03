#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    :param matrix: A 2-dimensional array.
    :return: A new matrix with each value being the square of
    the input.
    """
    return [[value ** 2 for value in row] for row in matrix]
