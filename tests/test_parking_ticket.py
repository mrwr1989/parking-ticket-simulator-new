"""Unit tests for the ParkingTicket class."""

import unittest

from parked_car import ParkedCar
from parking_ticket import ParkingTicket


class MockOfficer:
    """Simple officer object used for ParkingTicket testing."""

    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number


class TestParkingTicket(unittest.TestCase):
    """Test the ParkingTicket class."""

    def setUp(self):
        """Create objects used by the tests."""
        self.car = ParkedCar(
            "Toyota", "Camry", "Blue", "ABC123", 90
        )
        self.officer = MockOfficer("John Smith", "1234")

    def test_car_and_officer_information(self):
        """Test that ticket contains correct car and officer information."""
        ticket = ParkingTicket(self.car, self.officer, 30)

        self.assertEqual(ticket.car.make, "Toyota")
        self.assertEqual(ticket.car.model, "Camry")
        self.assertEqual(ticket.car.color, "Blue")
        self.assertEqual(ticket.car.license_number, "ABC123")
        self.assertEqual(ticket.officer.name, "John Smith")
        self.assertEqual(ticket.officer.badge_number, "1234")

    def test_illegal_minutes(self):
        """Test that illegal minutes are stored correctly."""
        ticket = ParkingTicket(self.car, self.officer, 30)
        self.assertEqual(ticket.illegal_minutes, 30)

    def test_fine_one_minute(self):
        """Test fine for one illegal minute."""
        ticket = ParkingTicket(self.car, self.officer, 1)
        self.assertEqual(ticket.fine, 25)

    def test_fine_sixty_minutes(self):
        """Test fine for sixty illegal minutes."""
        ticket = ParkingTicket(self.car, self.officer, 60)
        self.assertEqual(ticket.fine, 25)

    def test_fine_sixty_one_minutes(self):
        """Test fine for sixty-one illegal minutes."""
        ticket = ParkingTicket(self.car, self.officer, 61)
        self.assertEqual(ticket.fine, 35)

    def test_fine_one_hundred_twenty_minutes(self):
        """Test fine for 120 illegal minutes."""
        ticket = ParkingTicket(self.car, self.officer, 120)
        self.assertEqual(ticket.fine, 35)

    def test_fine_one_hundred_twenty_one_minutes(self):
        """Test fine for 121 illegal minutes."""
        ticket = ParkingTicket(self.car, self.officer, 121)
        self.assertEqual(ticket.fine, 45)

    def test_readable_report(self):
        """Test that the ticket report contains required information."""
        ticket = ParkingTicket(self.car, self.officer, 30)
        report = str(ticket)

        self.assertIn("Toyota", report)
        self.assertIn("Camry", report)
        self.assertIn("Blue", report)
        self.assertIn("ABC123", report)
        self.assertIn("30", report)
        self.assertIn("$25.00", report)
        self.assertIn("John Smith", report)
        self.assertIn("1234", report)

    def test_invalid_illegal_minutes(self):
        """Test that zero illegal minutes are rejected."""
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, 0)


if __name__ == "__main__":
    unittest.main()