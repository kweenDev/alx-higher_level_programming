#!/usr/bin/python3
"""
Divide a list module
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element two lists and return a new list with the results
    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: length of the new list
    Returns:
        A new list with the results of the divisions
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            print("division by 0" if isinstance(
                my_list_2[i], int) and my_list_2[i] == 0 else "wrong type")
            result = 0
        except (IndexError):
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
