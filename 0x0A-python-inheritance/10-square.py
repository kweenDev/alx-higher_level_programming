#!/usr/bin/python3
"""
    This module creates a class that inherits from Rectangle.
"""


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
