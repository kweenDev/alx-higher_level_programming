#!/usr/bin/python3
"""
Prints the ASCII alphabet in lowercase, excluding 'q' and 'e'.
"""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
