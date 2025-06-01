# tests/test_converter.py

import unittest
from src.converter import km_to_miles, miles_to_km


class TestConverter(unittest.TestCase):

    def test_km_to_miles(self):
        self.assertAlmostEqual(km_to_miles(1), 0.621371, places=5)

    def test_miles_to_km(self):
        self.assertAlmostEqual(miles_to_km(1), 1.60934, places=5)

    def test_km_to_miles_negative(self):
        with self.assertRaises(ValueError):
            km_to_miles(-1)

    def test_miles_to_km_negative(self):
        with self.assertRaises(ValueError):
            miles_to_km(-5)


if __name__ == '__main__':
    unittest.main()
