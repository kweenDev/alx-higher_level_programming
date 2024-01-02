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
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Ensure the original list is not modified
    return my_list[:idx] + my_list[idx+1:]

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    # Test case 1
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)

    # Test case 2
    idx = 0
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)

    # Test case 3
    idx = 4
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)

    # Test case 4
    idx = 5
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)

    # Test case 5
    idx = -1
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)

    # Test case 6
    my_list = []
    idx = 0
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
