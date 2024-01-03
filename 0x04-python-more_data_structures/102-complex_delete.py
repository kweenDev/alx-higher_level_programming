#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    :param my_list: The input list.
    :param idx: The index to delete.
    :return: The modified list.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
