#!/usr/bin/python3
"""Module adds command-line args to list and saves to JSON file"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_items_to_list(filename, *args):
    """
    Adds command-line arguments to a Python list and saves them to a JSON file.
    """
    try:
        existing_list = load_from_json_file(filename)
    except FileNotFoundError:
        existing_list = []

    updated_list = existing_list + list(args)
    save_to_json_file(updated_list, filename)

if __name__ == "__main__":
    filename = "add_item.json"
    add_items_to_list(filename, *sys.argv[1:])
