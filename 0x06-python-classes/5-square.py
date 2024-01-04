#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Square class with private size attribute, size validation,
    area calculation, access/update capabilities for size attribute,
    and a method to print the square
    """

    def __init__(self, size=0):
        """Initialize a new instance of the Square class with optional size"""
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method to calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method to print the square using '#' characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
