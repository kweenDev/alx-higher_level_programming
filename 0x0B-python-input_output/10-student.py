#!/usr/bin/python3
"""Module extends Student class with JSON serialization & deserialization"""


class Student:
    """Defines a student with first_name, last_name, and age attributes."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age - age

    def to_json(self. attrs=None):
        """
        Retrieves a dictionary representation of a Student instance with
        optional attribute filtering.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
