#!/usr/bin/python3


def print_alphabet():
    """
    Prints the ASCII alphabet is lowercase, excluding 'q' and
    'e'.
    """
    for char in range(ord('a'), ord('z') + 1):
        if chr(char) not in ['q', 'e']:
            print(chr(char), end="")


if __name__ == "__main__":
    print_alphabet()
