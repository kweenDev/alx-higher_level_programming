#!/usr/bin/python3
"""
Safe printing of an integers list module
"""


def safe_print_integer(value):
    """
    Print an integer with "{:d}".format()
    Args:
        value: value to print
    Returns:
        True if value has been correctly printed as an integer,
        otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
