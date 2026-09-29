"""Unit tests for the PoliceOfficer class."""

import unittest

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer
from parking_ticket import ParkingTicket


class TestPoliceOfficer(unittest.TestCase):
    """Test the PoliceOfficer class and parking inspections."""

    def setUp(self):
        """Create an officer used by the tests."""
        self.officer = PoliceOfficer("John Smith", "1234")

    def test_less_than_purchased_time(self):
        """Test that no ticket is issued when parked time is less."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 30)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect(car, meter)

        self.assertIsNone(ticket)

    def test_exactly_purchased_time(self):
        """Test that no ticket is issued when parked time equals purchased time."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 60)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect(car, meter)

        self.assertIsNone(ticket)

    def test_one_minute_over_time(self):
        """Test that a ticket is issued when one minute over."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 61)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect(car, meter)

        self.assertIsInstance(ticket, ParkingTicket)

    def test_illegal_minutes(self):
        """Test that the ticket contains the correct illegal minutes."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 90)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect(car, meter)

        self.assertEqual(ticket.illegal_minutes, 30)

    def test_ticket_car_information(self):
        """Test that the ticket contains the expected car."""
        car = ParkedCar("Honda", "Accord", "Black", "XYZ789", 90)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect(car, meter)

        self.assertEqual(ticket.car, car)
        self.assertEqual(ticket.car.license_number, "XYZ789")

    def test_ticket_officer_information(self):
        """Test that the ticket contains the expected officer."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 90)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect(car, meter)

        self.assertEqual(ticket.officer, self.officer)
        self.assertEqual(ticket.officer.name, "John Smith")
        self.assertEqual(ticket.officer.badge_number, "1234")


if __name__ == "__main__":
    unittest.main()