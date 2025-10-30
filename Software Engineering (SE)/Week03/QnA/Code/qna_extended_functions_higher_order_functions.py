"""
Ride Sharing System
------------------
This program implements a ride-sharing service that helps match riders with nearby drivers based on
distance and fare criteria. It includes functionality to filter drivers by distance, calculate total
trip distances, validate inputs, and find the most economical option for the rider.

Key features:
- Filter drivers within a specified radius
- Calculate total trip distances
- Validate distance and fare inputs
- Display driver information
- Calculate average fares
- Find the driver with the lowest fare
"""

from functools import reduce

# Sample data structure for a rider
rider = {
    "name": "User1",
    "location": "Cape Town",
    "destination": "Stellenbosch"
}

# List of available drivers with their details
drivers = [
    {"name": "Ayanda", "distance_to_rider": 1.5, "fare": 80},
    {"name": "Brad", "distance_to_rider": 4.2, "fare": 120},
    {"name": "Candice", "distance_to_rider": 2.8, "fare": 95},
    {"name": "Dumi", "distance_to_rider": 0.9, "fare": 70},
    {"name": "Ebrahim", "distance_to_rider": 5.1, "fare": 150},
]

# Constants for distance calculations
destination_distance = 15  # Distance in kilometers to the destination
distance_radius = 3      # Maximum acceptable distance to pick up rider

def filter_nearby_drivers(drivers, max_distance=distance_radius):
    """
    Filter drivers who are within the specified maximum distance from the rider.

    Args:
        drivers (list): List of driver dictionaries containing their details
        max_distance (float): Maximum acceptable distance in kilometers (default: distance_radius)

    Returns:
        list: Filtered list of drivers within the specified radius
    """
    nearby_drivers = filter(lambda driver: driver["distance_to_rider"] <= max_distance, drivers)
    return list(nearby_drivers)

def add_total_distance(driver, destination_distance):
    """
    Calculate and add the total trip distance to a driver's information.

    Args:
        driver (dict): Dictionary containing driver's information
        destination_distance (float): Distance to the final destination in kilometers

    Returns:
        dict: Updated driver dictionary with total_distance added
    """
    total_distance = calculate_total_distance(driver["distance_to_rider"], destination_distance)
    driver["total_distance"] = total_distance
    return driver

def validate_positive(func):
    """
    Decorator that validates if all numeric arguments are positive.

    Args:
        func: The function to be decorated

    Returns:
        wrapper: The wrapped function that includes validation

    Raises:
        ValueError: If any numeric argument is negative

    Note:
        *args: Variable positional arguments passed to the decorated function
        **kwargs: Variable keyword arguments passed to the decorated function
    """
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Distances and fares cannot be negative.")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_total_distance(distance_to_rider, destination_distance):
    """
    Calculate the total distance for a trip.

    Args:
        distance_to_rider (float): Distance from driver to rider in kilometers
        destination_distance (float): Distance from pickup to destination in kilometers

    Returns:
        float: Total distance of the trip
    """
    return distance_to_rider + destination_distance

def display_driver(driver):
    """
    Format driver information for display.

    Args:
        driver (dict): Dictionary containing driver's information

    Returns:
        str: Formatted string with driver details

    """
    return f"{driver['name']} (Distance to Rider: {driver['distance_to_rider']}km, Total Distance: {driver.get('total_distance', 'N/A')} km, Fare: {driver['fare']} units)"

def calculate_average_fare(drivers):
    """
    Calculate the average fare across all provided drivers.

    Args:
        drivers (list): List of driver dictionaries

    Returns:
        float: Average fare amount
    """
    fares = map(lambda driver: driver["fare"], drivers)
    avg_fares = reduce(lambda acc, fare: acc + fare, fares, 0) / len(drivers)
    return avg_fares

def find_driver_with_lowest_fare(drivers):
    """
    Find the driver offering the lowest fare.

    Args:
        drivers (list): List of driver dictionaries

    Returns:
        dict: Driver dictionary with the lowest fare
    """
    return min(drivers, key=lambda driver: driver["fare"])

# Main execution flow
# Filter drivers within the acceptable radius
nearby_drivers = filter_nearby_drivers(drivers)

# Calculate total distances for nearby drivers using map
drivers_with_total_distance = list(map(
    lambda driver: add_total_distance(driver, destination_distance),
    nearby_drivers
))

# Display information about nearby drivers
print("Nearby Drivers:")
nearby_drivers_list = list(map(display_driver, drivers_with_total_distance))
for driver in nearby_drivers_list:
    print(driver)

# Calculate and display average fare
average_fare = calculate_average_fare(drivers_with_total_distance)
print(f"Average fare: {average_fare:.2f} units")  # .2f formats the float to 2 decimal places

# Find and display the best driver based on lowest fare
best_driver = find_driver_with_lowest_fare(drivers_with_total_distance)

if best_driver:
    """
    This conditional statement checks if a best driver was found.
    If find_driver_with_lowest_fare() returns a driver (a dictionary), best_driver will evaluate to True.
    If no drivers were found (the list was empty), find_driver_with_lowest_fare() returns None, and best_driver evaluates to False.
    """
    print(f"Best Driver (lowest fare): {display_driver(best_driver)}")
else:
    """
    This 'else' block executes only if best_driver is False (i.e., no drivers were found).
    """
    print("No drivers available.")