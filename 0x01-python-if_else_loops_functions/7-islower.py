#!/usr/bin/python3


def islower(c):
    """
    Checks if a character is lowercase.
    Args:
    - c (str): The character to check.
    Returns:
    - bool: True if c is lowercase, False otherwise.
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
