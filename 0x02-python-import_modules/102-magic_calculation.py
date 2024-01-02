#!/usr/bin/python3


def magic_calculation(a, b):
    if a < b:
        return magic_calculation_102.add(a, b) + sum(range(4, 6))
    return magic_calculation_102.sub(a, b)
