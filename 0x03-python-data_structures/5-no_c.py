#!/usr/bin/python3


def no_c(my_string):
    """
    Remove all characters 'c' and 'C' from a string.

    Args:
    - my_string: Input string.

    Returns:
    - A new string with 'c' and 'C' removed.
    """
    return ''.join(char for char in my_string if char.lower() not in ('c', 'C'))


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
