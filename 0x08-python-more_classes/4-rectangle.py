# Importing the Rectangle class from the previous module
from rectangle import Rectangle


def create_rectangle_from_user_input():
    """
    Takes user input for width and height to create a Rectangle object.
    Adheres to PEP8 and pycodestyle.
    """
    try:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        # Creating a Rectangle object with user-provided values
        user_rectangle = Rectangle(width, height)
        return user_rectangle
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return None
