#!/usr/bin/python3
"""
ByteCode to Python #4 module
"""


def magic_calculation(a, b):
    """
    Simulates the given Python bytecode
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError("Too far")  # Using a more specific exception
            result += (a ** b) / i
        except ZeroDivisionError as zde:  # Handling division by zero
            print(f"Caught a ZeroDivisionError: {zde}")
            result = b + a
            break
        except ValueError as ve:  # Handling the custom "Too far" exception
            print(f"Caught a ValueError: {ve}")
            result = b + a
            break
    return result

# Example usage
result = magic_calculation(2, 3)
print(f"Result: {result}")
