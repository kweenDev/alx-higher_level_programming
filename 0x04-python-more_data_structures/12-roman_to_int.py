#!/usr/bin/python3


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    :param roman_string: The input Roman numeral string.
    :return: The corresponding integer value.
    """
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        arabic = digits[roman]
        total += arabic if total < arabic * 5 else -arabic
        return total
