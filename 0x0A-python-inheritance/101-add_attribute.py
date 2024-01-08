#!/usr/bin/python3
"""
    This module adds a new attribute to an object if possible.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: An object.
        name: A string representing the attribute name.
        value: The value to be assigned to the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
