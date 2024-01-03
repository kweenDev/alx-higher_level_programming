#!/usr/bin/python3
"""
Safe function module
"""

import sys


def safe_function(fct, *args):
    """
    Executes a function safely and returns the result.
    Args:
        fct: The function to be executed
        *args: Arguments to be passed to the function
    Returns:
        The result of the function if successful, None otherwise with
        an error message.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
