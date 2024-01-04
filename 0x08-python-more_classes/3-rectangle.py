# Importing the Rectangle class from the previous module
from rectangle import Rectangle


class Rectangle:
    """
    Extends the previous Rectangle class with a string representation method.
    Adheres to PEP8 and pycodestyle.
    """
    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return (f"Rectangle(width={self.__width}, height={self.__height})")
