#!/usr/bin/python3
"""Module extends Student class with file serialization and deserialization"""


class Student:
    """Defines a student with first_name, last_name, and age attributes."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instnace with
        option attribute filtering.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on
        the provided dictionary.
        """
        for k, v in json.items():
            setattr(self, k, v)
