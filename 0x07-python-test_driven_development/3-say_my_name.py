#!/usr/bin/python3
"""
Module for printing a name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the given first and last name.

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
