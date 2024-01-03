#!/usr/bin/python3


def multiply_list_map(my_list=[], multiplier=0):
    """
    Multiplies all elements of a list by a specified multiplier using map.

    :param my_list: The input list.
    :param multiplier: The multiplier to apply.
    :return: A new list with elements multiplied.
    """
    return list(map(lambda x: x * multiplier, my_list))
