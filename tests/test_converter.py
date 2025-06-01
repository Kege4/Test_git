# tests/test_converter.py

import unittest
from src.converter import km_to_miles, miles_to_km


class TestConverter(unittest.TestCase):

    def test_km_to_miles_valid(self):
        self.assertEqual(km_to_miles(5), 3.107)

    def test_miles_to_km_valid(self):
        self.assertEqual(miles_to_km(3.107), 5.0)

    def test_km_to_miles_negative(self):
        with self.assertRaises(ValueError):
            km_to_miles(-1)

    def test_miles_to_km_negative(self):
        with self.assertRaises(ValueError):
            miles_to_km(-5)


if __name__ == "__main__":
    unittest.main()
