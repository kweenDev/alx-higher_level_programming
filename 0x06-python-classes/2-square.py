#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Square class with private size attribute and size validation"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
