#!/usr/bin/python3
"""Inserts line of text into file after specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string.
    """
    updated_lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            updated_lines.append(line)
            if search_string in line:
                updated_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(updated_lines)
