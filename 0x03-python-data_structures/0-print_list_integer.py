#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.

    :param my_list: List of integers
    :return: None
    """
    for num in my_list:
        print("{:d}".format(num))

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
