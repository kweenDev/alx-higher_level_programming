#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a specific position.

    Args:
    - my_list: The input list.
    - idx: Index of the element to replace.
    - element: The new element.

    Returns:
    - The modified list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)
    print(new_list)
    print(my_list)
