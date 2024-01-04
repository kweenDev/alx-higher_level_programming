#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Square class with private size attribute, size validation, and area calculation"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class with optional size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method to calculate the area of the square"""
        return self.__size ** 2
