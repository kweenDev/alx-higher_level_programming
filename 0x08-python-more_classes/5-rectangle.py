# Importing the Rectangle class from the previous module
from rectangle import Rectangle


def calculate_area_and_perimeter(rectangle):
    """
    Calculates the area and perimeter of a given Rectangle object.
    Adheres to PEP8 and pycodestyle.
    
    Parameters:
    rectangle (Rectangle): The Rectangle object for which to calculate area and perimeter.
    
    Returns:
    tuple: A tuple containing the area and perimeter values.
    """
    area = rectangle.calculate_area()
    perimeter = rectangle.calculate_perimeter()
    return area, perimeter


def display_area_and_perimeter(rectangle):
    """
    Displays the area and perimeter of a given Rectangle object.
    Adheres to PEP8 and pycodestyle.
    
    Parameters:
    rectangle (Rectangle): The Rectangle object to display area and perimeter for.
    """
    area, perimeter = calculate_area_and_perimeter(rectangle)
    print(f"Area: {area}, Perimeter: {perimeter}")
