#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """
    Deletes the item at a specific position in a list.

    :param a_dictionary: The input.
    :param value: The value to be deleted.
    :return: The modified dictionary.
    """
    if 0 <= value < len(a_dictionary):
        del a_dictionary[value]
    return a_dictionary
