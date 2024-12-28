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

def filter_nearby_drivers_no_hof(drivers, max_distance):
    """
    Filters drivers who are within the specified maximum distance radius from the rider.

    Args:
        drivers (list): List of driver dictionaries.
        max_distance (float): Maximum distance in kilometers to consider a driver as nearby.

    Returns:
        list: A list of drivers within the specified distance radius.
    """
    nearby_drivers = []
    for driver in drivers:
        if driver["distance_to_rider"] <= max_distance:
            nearby_drivers.append(driver)
    return nearby_drivers

def add_total_distance_no_hof(drivers, destination_distance):
    """
    Adds total distances (to rider + to destination) for all drivers.

    Args:
        drivers (list): List of driver dictionaries.
        destination_distance (float): Distance from the rider's location to the destination.

    Returns:
        list: List of drivers with updated total distance.
    """
    for driver in drivers:
        driver["total_distance"] = driver["distance_to_rider"] + destination_distance
    return drivers

def calculate_average_fare_no_hof(drivers):
    """
    Calculates the average fare from a list of drivers.

    Args:
        drivers (list): List of driver dictionaries.

    Returns:
        float: The average fare of the drivers.
    """
    total_fare = 0
    for driver in drivers:
        total_fare += driver["fare"]
    return total_fare / len(drivers)

def find_driver_with_lowest_fare_no_hof(drivers):
    """
    Identifies the driver with the lowest fare from a list of drivers.

    Args:
        drivers (list): List of driver dictionaries.

    Returns:
        dict: The driver dictionary with the lowest fare.
    """
    lowest_fare_driver = drivers[0]
    for driver in drivers:
        if driver["fare"] < lowest_fare_driver["fare"]:
            lowest_fare_driver = driver
    return lowest_fare_driver

def display_driver_no_hof(driver):
    """
    Formats and returns a driver's information as a string for display.

    Args:
        driver (dict): A dictionary representing a driver.

    Returns:
        str: Formatted string with driver details, including distance and fare.
    """
    return f"{driver['name']} (Distance to Rider: {driver['distance_to_rider']}km, Total Distance: {driver.get('total_distance', 'N/A')} km, Fare: {driver['fare']} units)"

# Main execution flow
# Filter drivers within the acceptable radius
nearby_drivers = filter_nearby_drivers_no_hof(drivers, distance_radius)

# Add total distances to the drivers
drivers_with_total_distance = add_total_distance_no_hof(nearby_drivers, destination_distance)

# Display information about nearby drivers
print("Nearby Drivers:")
for driver in drivers_with_total_distance:
    print(display_driver_no_hof(driver))

# Calculate and display average fare
average_fare = calculate_average_fare_no_hof(drivers_with_total_distance)
print(f"Average fare: {average_fare:.2f} units")  # .2f formats the float to 2 decimal places

# Find and display the best driver based on lowest fare
best_driver = find_driver_with_lowest_fare_no_hof(drivers_with_total_distance)

if best_driver:
    print(f"Best Driver (lowest fare): {display_driver_no_hof(best_driver)}")
else:
    print("No drivers available.")
