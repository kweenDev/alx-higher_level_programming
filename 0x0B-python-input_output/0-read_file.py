#!/usr/bin/python3
"""Module reads and prints content of a text file."""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
