# Importing the Rectangle class from the previous module
from rectangle import Rectangle


class InvalidDimensionsError(Exception):
    """
    Custom exception to raise when invalid dimensions are
    provided for a Rectangle.
    Adheres to PEP8 and pycodestyle.
    """
    def __init__(
            self, message="Invalid dimensions for Rectangle.
            Length and width must be positive numbers."):
        super().__init__(message)

class RectangleWithValidation(Rectangle):
    """
    Rectangle class with added validation for dimensions.
    Adheres to PEP8 and pycodestyle.
    """
    def __init__(self, length, width):
        """
        Initializes the RectangleWithValidation object with
        validated dimensions.
        
        Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
        Raises:
        InvalidDimensionsError: If invalid dimensions are provided.
        """
        self.validate_dimensions(length, width)
        super().__init__(length, width)


    def validate_dimensions(self, length, width):
        """
        Validates the dimensions of the rectangle.
        
        Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
        Raises:
        InvalidDimensionsError: If invalid dimensions are provided.
        """
        if length <= 0 or width <= 0:
            raise InvalidDimensionsError()
