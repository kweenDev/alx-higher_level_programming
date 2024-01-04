# Importing necessary modules
import logging


# Configuring the logging module
logging.basicConfig(
        filename='rectangle_log.txt', level=logging.INFO, format=
        '%(asctime)s - %(levelname)s - %(message)s')

class RectangleWithLogging(RectangleWithValidation):
    """
    Rectangle class with integrated logging for actions.
    Adheres to PEP8 and pycodestyle.
    """
    def __init__(self, length, width):
        """
        Initializes the RectangleWithLogging object with
        validated dimensions and logs the creation.
        
        Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        """
        super().__init__(length, width)
        logging.info(f"Rectangle created with dimensions:
                Length - {length}, Width - {width}")

    def calculate_area(self):
        """
        Calculates the area of the rectangle and logs the action.
        
        Returns:
        float: The area of the rectangle.
        """
        area = super().calculate_area()
        logging.info(f"Area calculated: {area}")
        return area
