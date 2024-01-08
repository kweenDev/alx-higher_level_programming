#!/usr/bin/python3
"""
    This module extends the BaseGeometry to create a Rectangle class.
"""


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry.
    Instantiation with width and height.

    Args:
        width: Width of the rectangle.
        height: Height of the rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
