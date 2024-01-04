#!/usr/bin/python3
"""Module that defines a MagicClass"""


import math


class MagicClass:
    """MagicClass that mimics the given Python bytecode"""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the MagicClass"""
        return 2 * math.pi * self.__radius
