#!/usr/bin/python3
"""Generates Pascal's Triangle up to a given number of rows"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        row = [1]
        for i in range(len(tri) - 1):
            row.append(tri[i] + tri[i + 1])
        row.append(1)
        triangle.append(row)

    return triangle
