#!/usr/bin/python3


def uppercase(str):
    """
    Checks if a character is uppercase.
    Args:
    - c (str): The character to check.
    Returns:
    - bool: True if c is uppercase, False otherwise.
    """
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
            print("")
