#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Square class with private size and position attributes,
    size and position validation, area calculation, access/update
    capabilities for size and position attributes, and a method to
    print the square with position
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new instance of the Square class with
        optional size and position"""
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
            not all(isinstance(coord, int) for coord in value) or
            any(coord < 0 for coord in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method to calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method to print the square with
        position using '#' characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
