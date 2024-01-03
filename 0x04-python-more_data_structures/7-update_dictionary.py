#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    :param a_dictionary: The input dictionary.
    :param key: The key to replace or add.
    :param value: The value associated with the key.
    :return: The modified dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
