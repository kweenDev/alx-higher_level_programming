#!/usr/bin/python3
"""
    This module creates a MyList class.
"""


class MyList(list):
    """
    A class that inherits from list.

    Public instance method:
        print_sorted(self): Prints the list, but sorted in ascending order.
    """
    def __init__(self):
        """
        Initializes the object
        """
        super().__init__()


    def print_sorted(self):
        print(sorted(self))
