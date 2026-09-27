"""Defines the ParkedCar class for the Parking Ticket Simulator."""


class ParkedCar:
    """Represents a car parked at a parking meter."""

    def __init__(self, make, model, color, license_number, minutes_parked):
        """Initialize a parked car with identifying information and parked time."""
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @property
    def make(self):
        """Return the make of the car."""
        return self._make

    @make.setter
    def make(self, value):
        """Set the make of the car."""
        self._make = self._validate_string(value, "make")

    @property
    def model(self):
        """Return the model of the car."""
        return self._model

    @model.setter
    def model(self, value):
        """Set the model of the car."""
        self._model = self._validate_string(value, "model")

    @property
    def color(self):
        """Return the color of the car."""
        return self._color

    @color.setter
    def color(self, value):
        """Set the color of the car."""
        self._color = self._validate_string(value, "color")

    @property
    def license_number(self):
        """Return the license number of the car."""
        return self._license_number

    @license_number.setter
    def license_number(self, value):
        """Set the license number of the car."""
        self._license_number = self._validate_string(value, "license number")

    @property
    def minutes_parked(self):
        """Return the number of minutes the car has been parked."""
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, value):
        """Set the number of minutes the car has been parked."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("minutes_parked must be an integer")
        if value < 0:
            raise ValueError("minutes_parked cannot be negative")
        self._minutes_parked = value

    @staticmethod
    def _validate_string(value, field_name):
        """Validate a required string value."""
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty")
        return value