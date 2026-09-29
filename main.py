"""Demonstrates the Parking Ticket Simulator."""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def main():
    """Run a demonstration of the parking ticket simulator."""

    # Create a parked car that has been parked for 125 minutes.
    car = ParkedCar(
        "Toyota",
        "Camry",
        "Blue",
        "ABC123",
        125
    )

    # Create a parking meter with 60 minutes purchased.
    meter = ParkingMeter(60)

    # Create the police officer.
    officer = PoliceOfficer("John Smith", "1234")

    # Have the officer inspect the parked car.
    ticket = officer.inspect(car, meter)

    # Display the result of the inspection.
    if ticket is not None:
        print(ticket)
    else:
        print("No parking violation.")


if __name__ == "__main__":
    main()