#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
    - my_list: List of integers.

    Returns:
    - A new list with True or False, depending on whether the integer
    at the same position in the original list is a multiple of 2.
    """
    return [num % 2 == 0 for num in my_list]


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)
    for i in range(len(list_result)):
        print("{:d} {:s} divisible by 2".format(
            my_list[i], "is" if list_result[i] else "is not"))
