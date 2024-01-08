#!/usr/bin/python3
"""
    This module extends the BaseGeometry with a method area.
"""


class BaseGeometry:
    """
    A class with a public instance method 'area' that raises an
    Exception with the message 'area() is not implemented'.
    """
    def area(self):
        raise Exception("area() is not implemented")
