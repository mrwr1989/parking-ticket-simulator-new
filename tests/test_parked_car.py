"""Unit tests for the ParkedCar class."""

import unittest

from parked_car import ParkedCar


class TestParkedCar(unittest.TestCase):
    """Test the ParkedCar class."""

    def test_valid_construction(self):
        """Test valid construction and property access."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 45)

        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.color, "Blue")
        self.assertEqual(car.license_number, "ABC123")
        self.assertEqual(car.minutes_parked, 45)

    def test_property_reassignment(self):
        """Test valid property reassignment."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 45)

        car.make = "Honda"
        car.model = "Accord"
        car.color = "Black"
        car.license_number = "XYZ789"
        car.minutes_parked = 60

        self.assertEqual(car.make, "Honda")
        self.assertEqual(car.model, "Accord")
        self.assertEqual(car.color, "Black")
        self.assertEqual(car.license_number, "XYZ789")
        self.assertEqual(car.minutes_parked, 60)

    def test_empty_string(self):
        """Test that an empty string is rejected."""
        with self.assertRaises(ValueError):
            ParkedCar("", "Camry", "Blue", "ABC123", 45)

    def test_incorrect_string_type(self):
        """Test that an incorrect string type is rejected."""
        with self.assertRaises(TypeError):
            ParkedCar(123, "Camry", "Blue", "ABC123", 45)

    def test_zero_minutes(self):
        """Test that zero parked minutes is valid."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 0)
        self.assertEqual(car.minutes_parked, 0)

    def test_positive_minutes(self):
        """Test that positive parked minutes are valid."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 30)
        self.assertEqual(car.minutes_parked, 30)

    def test_negative_minutes(self):
        """Test that negative parked minutes are rejected."""
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Camry", "Blue", "ABC123", -1)

    def test_noninteger_minutes(self):
        """Test that noninteger parked minutes are rejected."""
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", "Blue", "ABC123", 30.5)


if __name__ == "__main__":
    unittest.main()