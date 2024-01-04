#!/usr/bin/python3
"""
Module that defines a Rectangle class with width and height attributes.
"""


class Rectangle:
    """
    Defines a Rectangle class with width and height attributes.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieves the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width attribute with the given value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height attribute with the given value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
