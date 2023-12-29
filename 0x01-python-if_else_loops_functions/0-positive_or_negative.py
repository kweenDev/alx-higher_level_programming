#!/usr/bin/python3
import random


def positive_or_negative():
    """
    Assigns a random signed number to the variable number and
    prints whether it is positive, negative, or zero.
    """
    number = random.randint(-10, 10)

    print(f"{number} ", end="")

    if number > 0:
        print("is positive")
    elif number == 0:
        print("is zero")
    else:
        print("is negative")


if __name__ == "__main__":
    positive_or_negative()
