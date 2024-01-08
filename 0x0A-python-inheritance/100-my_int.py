#!/usr/bin/python3
"""
    This module inherits with inverted equality and inequality operators.
"""


class MyInt(int):
    """
    A class that inherits from int.
    MyInt is a rebel. It has == and != operators inverted.
    """
    def __eq__(self, other):
        """
        Override the equality operator.

        Args:
            other: Another object.

        Returns:
            True if the objects are not equal, else False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator.

        Args:
            other: Another object.

        Returns:
            True if the objects are equal, else False.
        """
        return super().__eq__(other)
