#!/usr/bin/python3
"""
    This module checks if an object is an instance of a class
    inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        True if obj is an instance of a class that inherits from
        a_class, else False.
    """
    return (isinstance(type(obj), a_class))
