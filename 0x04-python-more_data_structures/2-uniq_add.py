#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    :param my_list: The input list.
    :return: The sum of unique integers.
    """
    return sum(set(my_list))
