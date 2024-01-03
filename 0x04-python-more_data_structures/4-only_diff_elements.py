#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    :param set_1: The first set.
    :param set_2: The second set.
    :return: A set of elements present in only one set.
    """
    return set_1.symmetric_difference(set_2)
