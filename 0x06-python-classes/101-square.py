#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Square class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position with validation"""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(val, int) for val in value) or
            any(val < 0 for val in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square for print()"""
        result = ""
        if self.__size == 0:
            return result
        for _ in range(self.__position[1]):
            result += "\n"
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.strip()
