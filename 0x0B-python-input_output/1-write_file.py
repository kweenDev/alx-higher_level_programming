#!/usr/bin/python3
"""Module writes content to a text file and returns the number of characters."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_charcters = file.write(text)
        return nb_characters
