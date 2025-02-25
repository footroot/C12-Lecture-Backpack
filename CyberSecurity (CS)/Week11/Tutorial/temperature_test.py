import unittest
from functions import celsius_to_fahrenheit

class TestConversionFunction(unittest.TestCase):

    def test_celsius_to_fahrenheit_normal_case(self):
        # Given/Arrange
        temp = 25
        # When/Act
        result = celsius_to_fahrenheit(temp)
        # Then/Assert
        self.assertEqual(result, 77.0)

    def test_celsius_to_fahrenheit_negative_value(self):
        temp = -10
        result = celsius_to_fahrenheit(temp)
        self.assertEqual(result, 14.0)

    def test_celsius_to_fahrenheit_invalid_value(self):
        temp = "cold"
        result = celsius_to_fahrenheit(temp)
        self.assertEqual(result, "Invalid input.")

if __name__ == "__main__":
    unittest.main()
