#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Args:
    - my_list: List of integers to be printed in reverse.
    """
     if my_list:
         for i in reversed(my_list):
             print('{:d}'.format(i))
