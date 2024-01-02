#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
    - my_list: List of elements.
    - idx: Index to delete.

    Returns:
    - A new list with the item at the specified position removed.
    """
    if 0 <= idx < len(my_list):
        del(my_list[idx])
    return (my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
