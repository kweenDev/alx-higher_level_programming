#!/usr/bin/python3
"""
    This module returns true or false if the object is an instance of
    or inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        True if obj is an instance of a_class or inherits from it,
        else False.
    """
    return (isinstance(obj, a_class))

