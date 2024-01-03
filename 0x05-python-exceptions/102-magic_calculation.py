#!/usr/bin/python3
"""
ByteCode to Python #4 module
"""


def magic_calculation(a, b):
    """
    Simulates the given Python bytecode
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except (TypeError, ZeroDivisionError):
            result = b + a
            break
    return result
