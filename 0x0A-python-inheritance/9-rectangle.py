#!/usr/bin/python3
"""
    This module enhances Rectangle with an area method and a custom string.
"""


class BaseGeometry:
    """
    A class with a public instance method 'area' that raises an
    Exception with the message 'area() is not implemented'.
    A public instance method 'integer_validator' that validates
    an integer value.

    Args:
        name: A string representing the attribute name.
        value: An integer value to be validated.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
