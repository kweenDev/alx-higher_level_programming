#!/usr/bin/python3
"""
    This module creates a class with an integer_validator method.
"""


class BaseGeometry:
    """
    A class with a public instance method 'area' that raises an
    Exception with the message 'area() is not implemented'.
    A public instance method 'integer_validator' that validates an
    integer value.

    Args:
        name: A string representing the attribute name.
        value: An integer value to be validated.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
