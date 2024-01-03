#!/usr/bin/python3
"""
Safe list printing module
"""

def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list
    Args:
        my_list: list to print elements from
        x: number of elements to print
    Returns:
        The real number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
