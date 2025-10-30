"""
This module defines a Car class to manage car information. It demonstrates the use of class attributes, instance attributes, instance methods, static methods, and class methods.
"""

class Car:
    """
    Represents a car with attributes and methods.

    Attributes:
        vehicle_id_number (int): A class attribute tracking the total number of cars created.
        manufacturer (str): A class attribute representing the car's manufacturer.

    Methods:
        __init__(color, model): Initializes a new Car object.
        display_details(): Returns a formatted string with the car's details.
        validate_vin(vin_number): A static method that validates a VIN number.
        update_manufacturer(new_manufacturer): A class method that updates the car manufacturer.
    """

    # Class attributes: Shared by all instances.
    vehicle_id_number = 0  # Tracks the total number of cars.
    manufacturer = "Generic Motors"  # Default manufacturer.

    def __init__(self, color, model):
        """
        Initializes a new Car object.

        Args:
            color (str): The color of the car.
            model (str): The model of the car.
        """
        # Instance attributes: Unique to each car.
        self.vin_number = f"XXXVVV1112223334{Car.vehicle_id_number}" # Generates a unique VIN
        self.color = color
        self.model = model
        Car.vehicle_id_number += 1  # Increment the car count.

    def display_details(self):
        """
        Returns a formatted string with the car's details.

        Returns:
            str: A formatted string containing the car's VIN, color, model, and manufacturer.
        """
        return (
            f"Car Details:\n"
            f"VIN: {self.vin_number}\n"
            f"Color: {self.color}\n"
            f"Model: {self.model}\n"
            f"Manufacturer: {Car.manufacturer}\n"
        )

    @staticmethod
    def validate_vin(vin_number):
        """
        Validates a VIN number.

        Args:
            vin_number (str): The VIN number to validate.

        Returns:
            str: "Valid" if the VIN is valid, "Invalid" otherwise.
        """
        if len(vin_number) == 17 and vin_number.isalnum():
            return "Valid"
        return "Invalid"

    @classmethod
    def update_manufacturer(cls, new_manufacturer):
        """
        Updates the manufacturer for all cars.

        Args:
            new_manufacturer (str): The new manufacturer name.
        """
        cls.manufacturer = new_manufacturer

if __name__ == "__main__":
    # Example Usage:
    car1 = Car("Red", "Sedan")  # Creates a Car object named car1 with color "Red" and model "Sedan"
    car2 = Car("Blue", "SUV")   # Creates a Car object named car2 with color "Blue" and model "SUV"
    car3 = Car("Grey", "Sedan") # Creates a Car object named car3 with color "Grey" and model "Sedan"

    print("Validating VINs:") # Prints a header for the VIN validation section
    print(f"Car 1 VIN {car1.vin_number}: {Car.validate_vin(car1.vin_number)}") # Validates and prints the validation result for car1's VIN
    print(f"Car 2 VIN {car2.vin_number}: {Car.validate_vin(car2.vin_number)}") # Validates and prints the validation result for car2's VIN
    print(f"Car 3 VIN {car3.vin_number}: {Car.validate_vin(car3.vin_number)}") # Validates and prints the validation result for car3's VIN

    print(car1.display_details())  # Prints the details of car1
    print(car2.display_details())  # Prints the details of car2
    print(car3.display_details())  # Prints the details of car3

    print("Updating manufacturer to 'Super Cars Inc.'...\n")
    Car.update_manufacturer("Super Cars Inc.")  # Updates the manufacturer for all Car objects

    print(car1.display_details())  # Prints the details of car1 again (showing the updated manufacturer)
    print(car2.display_details())  # Prints the details of car2 again (showing the updated manufacturer)
    print(car3.display_details())  # Prints the details of car3 again (showing the updated manufacturer)

    print(f"Total cars created: {Car.vehicle_id_number}")  # Prints the total number of Car objects created