#!/usr/bin/python3
import json
"""Module converts an object to JSON representation."""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """
    return json.dumps(my_obj)
