#!/usr/bin/python3
"""Module extends Student class with JSON serialization & deserialization"""


class Student:
    """Defines a students attributes."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self. attrs=None):
        """
        Retrieves a dictionary representation of a Student
        instance with optional attribute filtering.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
