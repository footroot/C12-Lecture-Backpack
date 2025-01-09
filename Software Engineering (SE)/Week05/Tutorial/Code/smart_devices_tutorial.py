"""
Exercise: Smart Device Home System

Objective:
This exercise models a "Smart Device" system to manage various connected devices in a smart home. 
Each device has attributes such as name, type, location, and power status. It also calculates 
total power consumption across all devices.

Concepts Covered:
1. Instance attributes for device-specific information (e.g., name, type, location, wattage).
2. Class attributes to track shared properties (e.g., total connected devices, total power consumption).
3. Instance methods to control device power state and retrieve device information.
4. Class methods to register devices and update global properties like power consumption.
5. Static methods to provide general utilities unrelated to specific instances.
6. Encapsulation using private attributes to protect the power status of devices.

"""

class SmartDevice:
    """
    A class to represent a smart device in a connected home system.
    Tracks device-specific details and global system information like power consumption.

    Class Attributes:
    - connected_devices: Tracks the total number of devices registered.
    - total_power_consumption: Tracks the total power usage across all devices.

    Instance Attributes:
    - name: The name of the device.
    - device_type: The type of device (e.g., Light, Thermostat).
    - location: The location of the device (e.g., Living Room, Kitchen).
    - wattage: The power consumption of the device in watts.
    - __power_status: (Private) Tracks whether the device is ON or OFF.

    """

    connected_devices = 0  # Class attribute: Total number of devices connected
    total_power_consumption = 0  # Class attribute: Total power consumption across devices

    def __init__(self, name, device_type, location, wattage=0):
        """
        Initializes a new smart device with the given details.

        Parameters:
        - name (str): The name of the device.
        - device_type (str): The type of device (e.g., Light, Thermostat).
        - location (str): The location of the device (e.g., Living Room).
        - wattage (int): The power consumption of the device in watts (default is 0).
        """
        self.name = name  # Instance attribute: Name of the device
        self.device_type = device_type  # Instance attribute: Type of device
        self.location = location  # Instance attribute: Location of the device
        self.__power_status = False  # Private attribute: Tracks if the device is ON/OFF
        self.wattage = wattage  # Instance attribute: Power consumption in watts

        SmartDevice.register_device()  # Automatically register the device when it's created

    def turn_on(self):
        """
        Turns the device ON if it is currently OFF.
        Updates the total power consumption accordingly.
        """
        if not self.__power_status:  # Only turn ON if it's currently OFF
            self.__power_status = True
            SmartDevice.update_total_power_consumption(self.wattage)
            print(f"{self.name} turned ON.")

    def turn_off(self):
        """
        Turns the device OFF if it is currently ON.
        Updates the total power consumption accordingly.
        """
        if self.__power_status:  # Only turn OFF if it's currently ON
            self.__power_status = False
            SmartDevice.update_total_power_consumption(-self.wattage)
            print(f"{self.name} turned OFF.")

    def get_status(self):
        """
        Retrieves the current status of the device.

        Returns:
        dict: A dictionary containing the device's name, type, location, power status, and wattage.
        """
        return {
            "name": self.name,
            "type": self.device_type,
            "location": self.location,
            "power_status": self.__power_status,
            "wattage": self.wattage
        }

    @classmethod
    def register_device(cls):
        """
        Class method to register a new device.
        Increments the total count of connected devices.
        """
        cls.connected_devices += 1
        print(f"Device registered. Total devices: {cls.connected_devices}")

    @classmethod
    def update_total_power_consumption(cls, wattage_change):
        """
        Class method to update the total power consumption.

        Parameters:
        - wattage_change (int): The change in power consumption (positive for ON, negative for OFF).
        """
        cls.total_power_consumption += wattage_change
        print(f"Total power consumption: {cls.total_power_consumption}W")

    @staticmethod
    def convert_celsius_to_fahrenheit(celsius):
        """
        Static method to convert temperature from Celsius to Fahrenheit.

        Parameters:
        - celsius (float): Temperature in Celsius.

        Returns:
        float: Temperature in Fahrenheit.
        """
        return (celsius * 9 / 5) + 32


# Example usage:

# Create three smart devices
living_room_light = SmartDevice("Living Room Light", "Light", "Living Room", 60)
kitchen_thermostat = SmartDevice("Kitchen Thermostat", "Thermostat", "Kitchen", 0)  # No wattage
bedroom_plug = SmartDevice("Bedroom Lamp Plug", "Plug", "Bedroom", 100)

# Turn ON the living room light
print(f"Switching on {living_room_light.name}")
living_room_light.turn_on()
print(living_room_light.get_status())  # Display status
living_room_light.turn_off()  # Turn OFF the light

# Convert temperature
print(f"Convert 25°C to Fahrenheit: {SmartDevice.convert_celsius_to_fahrenheit(25)}")

# Turn ON and display the status of the thermostat
kitchen_thermostat.turn_on()
print(kitchen_thermostat.get_status())

# Operate the bedroom plug
bedroom_plug.turn_on()
bedroom_plug.turn_off()

# Display system-wide stats
print(f"Total connected devices: {SmartDevice.connected_devices}")
print(f"Total power consumption: {SmartDevice.total_power_consumption}")
