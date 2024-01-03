#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    Computes the weighted average of a list of tuples.

    :param my_list: List of tuples where each tuple contains
    (value, weight).
    :return: The weighted average.
    """
    if not my_list:
        return 0

    sum_values = sum(value * weight for value, weight in my_list)
    sum_weights = sum(weight for _, weight in my_list)

    return sum_values / sum_weights
