"""Defines the ParkingTicket class for the Parking Ticket Simulator."""

import math


class ParkingTicket:
    """Represents a parking citation issued for an expired parking meter."""

    def __init__(self, car, officer, illegal_minutes):
        """Initialize a parking ticket for a parking violation."""
        self._car = car
        self._officer = officer
        self.illegal_minutes = illegal_minutes

    @property
    def car(self):
        """Return the parked car associated with the ticket."""
        return self._car

    @property
    def officer(self):
        """Return the police officer who issued the ticket."""
        return self._officer

    @property
    def illegal_minutes(self):
        """Return the number of illegally parked minutes."""
        return self._illegal_minutes

    @illegal_minutes.setter
    def illegal_minutes(self, value):
        """Set and validate the number of illegally parked minutes."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("illegal_minutes must be an integer")

        if value <= 0:
            raise ValueError("illegal_minutes must be greater than zero")

        self._illegal_minutes = value

    @property
    def fine(self):
        """Calculate and return the parking fine."""
        if self.illegal_minutes <= 60:
            return 25

        additional_hours = math.ceil((self.illegal_minutes - 60) / 60)
        return 25 + (additional_hours * 10)

    def __str__(self):
        """Return a readable parking ticket report."""
        return (
            "PARKING TICKET\n"
            f"Make: {self.car.make}\n"
            f"Model: {self.car.model}\n"
            f"Color: {self.car.color}\n"
            f"License Number: {self.car.license_number}\n"
            f"Illegal Minutes: {self.illegal_minutes}\n"
            f"Fine: ${self.fine:.2f}\n"
            f"Officer: {self.officer.name}\n"
            f"Badge Number: {self.officer.badge_number}"
        )