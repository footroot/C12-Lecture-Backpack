# Demonstrating Classes and Objects in Python with Vehicles

# 1 & 2. Defining a Class and the __init__ Method (Constructor)
# A class is a blueprint for creating objects. Think of it like a template.
class Vehicle:
    # __init__ is the constructor. It's called automatically when you create a new Vehicle object.
    # self refers to the specific Vehicle object being created.
    def __init__(self, make, model, year, color):
        # These are instance attributes - data specific to each vehicle.
        self.make = make      # Make of the vehicle (e.g., "Toyota")
        self.model = model    # Model of the vehicle (e.g., "Camry")
        self.year = year      # Year the vehicle was made
        self.color = color    # Color of the vehicle
        self._current_speed = 0  # Current speed (starts at 0). The underscore "_" indicates this is intended for internal use (encapsulation).
        self._fuel_level = 100 # Fuel level (starts at 100). The underscore "_" indicates this is intended for internal use (encapsulation).

    # 3. Interacting with Objects (Dot Operator) and 5. The Importance of self
    # These are methods (functions that belong to the class).
    # self is always the first parameter and refers to the object calling the method.
    def accelerate(self, speed_increase):
        self._current_speed += speed_increase # Increases the vehicle's speed.
        print(f"The {self.make} {self.model} is now going {self._current_speed} mph.")

    def display_info(self):
        return f"{self.year} {self.make} {self.model}" # Returns a formatted string with the car's information.

    def brake(self, speed_decrease):
        self._current_speed -= speed_decrease # Decreases the vehicle's speed.
        if self._current_speed < 0: # Ensures speed doesn't go below 0.
            self._current_speed = 0
        print(f"The {self.make} {self.model} is now going {self._current_speed} mph.")

    def refuel(self, fuel_added):
        self._fuel_level += fuel_added # Increases the vehicle's fuel level.
        if self._fuel_level > 100: # Ensures fuel level doesn't go above 100.
            self._fuel_level = 100
        print(f"The {self.make} {self.model} fuel level is now {self._fuel_level}%.")

    # 4. Encapsulation (Private Attributes and Getters/Setters)
    # Encapsulation means hiding the internal details of an object and providing controlled access.
    # Getters and setters are methods used to access and modify private attributes.
    def get_current_speed(self): #Getter - Method to get the current speed
        return self._current_speed

    def set_current_speed(self, speed): #Setter - Method to set the current speed with input validation
        if type(speed) == int and speed >= 0:
            self._current_speed = speed
        else:
            print("Speed must be a non-negative integer.")

    def get_fuel_level(self): #Getter - Method to get the fuel level
        return self._fuel_level

    def set_fuel_level(self, fuel): #Setter - Method to set the fuel level with input validation
        if type(fuel) == int and 0 <= fuel <= 100:
            self._fuel_level = fuel
        else:
            print("Fuel level must be an integer between 0 and 100.")
            
    def __str__(self): #String representation - Method to print the object in a user-friendly way.
        return f"{self.year} {self.color} {self.make} {self.model} (Speed: {self._current_speed} mph, Fuel: {self._fuel_level}%)"

# 6. Creating Objects (Instances)
# Creating two Vehicle objects (instances of the Vehicle class).
my_car = Vehicle("Toyota", "Camry", 2020, "Silver")
my_bike = Vehicle("Harley-Davidson", "Sportster", 2022, "Black")

# 3. Interacting with Objects (Dot Operator)
print(my_car.make)      # Accessing the 'make' attribute of the my_car object.
# Method Calls and Expected Outputs
print(my_car.display_info()) #Calling the display information method
my_car.accelerate(30)  # Calling the 'accelerate' method on my_car.
my_car.brake(10)       # Calling the 'brake' method on my_car.
my_car.accelerate(70)
my_car.brake(100)

# 4. Encapsulation
# print(my_car._current_speed)  # Direct access (possible but discouraged because of encapsulation)
print(my_car.get_current_speed()) # Using the getter (correct way to access)
my_car.set_current_speed(60) # Using the setter (correct way to modify with validation)
print(my_car.get_current_speed())
my_car.set_current_speed(-10) # Input validation
print(my_car.get_current_speed())
print(my_car.get_fuel_level())
my_car.refuel(20)
print(my_car.get_fuel_level())
my_car.set_fuel_level(150) # Input validation
print(my_car.get_fuel_level())
my_car.set_fuel_level("Full") # Input validation
print(my_car.get_fuel_level())

# 7. The Concept of Objects (State, Behavior, Identity, Lifecycle)
# Each object has:
# - State: The current values of its attributes (e.g., make, model, speed).
# - Behavior: What it can do (its methods, e.g., accelerate, brake).
# - Identity: Each object is unique in memory.
# - Lifecycle: Objects are created, used, and eventually cease to exist.
print(my_car) #Printing the object using the __str__ method
print(my_bike)
print(my_car is my_bike)  # Different objects, different identities (This will print False)

#Procedural Approach
#This is an example of how you would do this without objects
def procedural_accelerate(make, model, current_speed, speed_increase):
    new_speed = current_speed + speed_increase
    print(f"The {make} {model} is now going {new_speed} mph.")

procedural_accelerate("Ford", "Mustang", 20, 30)

# 8. Procedural vs. Object-Oriented Programming (Demonstrated)
# This shows the difference between doing it with and without classes.
# The object oriented way keeps related data and functions together in a more organised and reusable way.