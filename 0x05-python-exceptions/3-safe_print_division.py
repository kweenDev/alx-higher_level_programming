#!/usr/bin/python3
"""
Integers division with debug module
"""


def safe_print_division(a, b):
    """
    Divide two integers and print the result
    Args:
        a: numerator
        b: denominator
    Returns:
        The value of the division, or None if division by zero
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (None)
