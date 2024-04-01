#!/usr/bin/python3
"""Module converts class object to JSON representation"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for
    JSON serialization of an object.
    """
    return obj.__dict__
