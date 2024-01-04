import unittest


class TestRectangleWithLogging(unittest.TestCase):
    """
    Unit tests for the RectangleWithLogging class.
    Adheres to PEP8 and pycodestyle.
    """

    def setUp(self):
        """
        Set up a test instance of RectangleWithLogging.
        """
        self.rectangle_test = RectangleWithLogging(5, 10)

    def test_area_calculation(self):
        """
        Test the correctness of the area calculation.
        """
        self.assertEqual(self.rectangle_test.calculate_area(), 50)

    def test_invalid_dimensions(self):
        """
        Test if InvalidDimensionsError is raised for invalid dimensions.
        """
        with self.assertRaises(InvalidDimensionsError):
            RectangleWithLogging(-5, 10)

    def test_logging(self):
        """
        Test if the creation and area calculation are logged.
        """
        with self.assertLogs('rectangle_log.txt', level='INFO') as log:
            rectangle = RectangleWithLogging(3, 6)
            rectangle.calculate_area()

            self.assertIn(f"INFO:root:Rectangle created with dimensions: Length - 3, Width - 6", log.output[0])
            self.assertIn(f"INFO:root:Area calculated: 18.0", log.output[1])
