#!/usr/bin/python3
"""
    This module returns the list of available attributes and methods
    of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        A list of attributes and methods.
    """
    return dir(obj)
