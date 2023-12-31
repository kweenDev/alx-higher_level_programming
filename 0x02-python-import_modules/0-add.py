#!/usr/bin/python3
a = 1
b = 2


# Import the add function from add_0.py
from add_0 import add


# Check if the program is the main one
if __name__ == "__main__":
    # Use the print function with string format to display the result of adding a and b
    print("{} + {} = {}".format(a, b, add(a, b)))
