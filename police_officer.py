"""Defines the PoliceOfficer class for the Parking Ticket Simulator."""

from parking_ticket import ParkingTicket


class PoliceOfficer:
    """Represents a police officer who inspects parked cars."""

    def __init__(self, name, badge_number):
        """Initialize a police officer with a name and badge number."""
        self.name = name
        self.badge_number = badge_number

    @property
    def name(self):
        """Return the officer's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set and validate the officer's name."""
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value.strip():
            raise ValueError("name cannot be empty")
        self._name = value

    @property
    def badge_number(self):
        """Return the officer's badge number."""
        return self._badge_number

    @badge_number.setter
    def badge_number(self, value):
        """Set and validate the officer's badge number."""
        if not isinstance(value, str):
            raise TypeError("badge_number must be a string")
        if not value.strip():
            raise ValueError("badge_number cannot be empty")
        self._badge_number = value

    def inspect(self, car, meter):
        """Inspect a parked car and return a ticket if a violation exists."""
        illegal_minutes = car.minutes_parked - meter.minutes_purchased

        if illegal_minutes <= 0:
            return None

        return ParkingTicket(car, self, illegal_minutes)