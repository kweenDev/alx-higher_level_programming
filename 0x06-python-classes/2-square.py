#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Square class with private size attribute and size validation"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class with optional size"""
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


# Additional method to display the dictionary representation
def dict_(self):
    """Returns a dictionary representation of the Square instance"""
    return {'_Square__size': self.__size}


# Attach the function to the class as a method
Square.dict_ = dict_
