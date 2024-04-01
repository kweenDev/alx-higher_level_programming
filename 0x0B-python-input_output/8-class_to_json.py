#!/usr/bin/python3
"""Module converts class object to JSON representation"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for
    JSON serialization of an object.
    """
    serializable_attributes = {}

    for attr_name in dir(obj):
        if not attr_name.startswith("__") and not callable(getattr(obj, attr_name)):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                serializable_attributes[attr_name] = attr_value

                return serializable_attributes
