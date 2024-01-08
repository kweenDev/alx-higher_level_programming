#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Lazy matrix multiplication using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        np.ndarray: Resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, or
        if elements are not numeric.
        ValueError: If m_a or m_b is empty or if matrices cannot be
        multiplied.
    """

    return (np.matmul(m_a, m_b))
