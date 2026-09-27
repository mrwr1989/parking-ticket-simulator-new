"""Defines the ParkingMeter class for the Parking Ticket Simulator."""


class ParkingMeter:
    """Represents a parking meter and its purchased parking time."""

    def __init__(self, minutes_purchased):
        """Initialize the parking meter with purchased minutes."""
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        """Return the number of purchased parking minutes."""
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, value):
        """Set and validate the number of purchased parking minutes."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("minutes_purchased must be an integer")

        if value < 0:
            raise ValueError("minutes_purchased cannot be negative")

        self._minutes_purchased = value