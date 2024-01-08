#!/usr/bin/python3
"""
    This module creates a class that inherits from Rectangle.
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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    A class that inherits from Rectangle.
    Instantiation with size.

    Args:
        size: Size of the square.
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
