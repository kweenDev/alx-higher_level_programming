#!/usr/bin/python3
import random


def last_digit():
    """
    Assigns a random signed number to the variable number and prints the
    last digit along with additional information.
    """
    number = random.randint(-10000, 10000)

    last_digit = abs(number) % 10

    print(f"Last digit of {number} is {last_digit}", end=" ")

    if last_digit > 5:
        print("and is greater than 5")
    elif last_digit == 0:
        print("and is 0")
    else:
        print(f"and is less than 6 and not 0")


if __name__ == "__main__":
    last_digit()
