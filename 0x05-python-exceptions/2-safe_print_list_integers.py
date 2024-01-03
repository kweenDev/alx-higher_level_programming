#!/usr/bin/python3
"""
Print and count integers module
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list containing only integers
    Args:
        my_list: list to print elements from
        x: number of elements to print
    Returns:
        The real number of integers printed
    """
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
