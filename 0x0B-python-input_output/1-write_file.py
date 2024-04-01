#!/usr/bin/python3
"""
Module writes content to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8).
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
