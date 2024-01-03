#!/usr/bin/python3
"""
Safe integer print with error message module
"""

import sys


def safe_print_integer_err(value):
    """
    Prints an integer safely and returns True if successful,
    else False with error message.
    Args:
        value: The value to be printed
    Returns:
        True if value is printed successfully, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
