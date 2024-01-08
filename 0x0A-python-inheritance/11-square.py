#!/usr/bin/python3
"""
    This module overrides string representation of the Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
