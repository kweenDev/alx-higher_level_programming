#!/usr/bin/python3


def switch(a, b):
    """
    Switches the values of variables a and b.

    Args:
    - a: First variable.
    - b: Second variable.
    """
    a, b = b, a
    print("a={} - b={}".format(a, b))


if __name__ == "__main__":
    a = 10
    b = 89
    switch(a, b)
