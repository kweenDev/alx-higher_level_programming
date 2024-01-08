#!/usr/bin/python3
"""
This module checks if an object is an exact instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the
    specified class; otherwise False.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        True if obj is an instance of a_class, else False.
    """
    return (type(obj) is a_class)
