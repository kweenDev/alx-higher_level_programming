#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Args:
    - my_list: List of integers to be printed in reverse.
    """
    for num in reversed(my_list):
        print(num)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
