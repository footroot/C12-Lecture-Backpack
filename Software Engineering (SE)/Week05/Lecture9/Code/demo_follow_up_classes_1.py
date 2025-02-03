# This code demonstrates the basics of object-oriented programming (OOP) in Python
# by creating a simple Car class.

# A class is like a blueprint or template for creating objects.
# Think of it like a cookie cutter - the class is the cutter, and the objects are the cookies.
class Car:
    # The __init__ method is a special method called the constructor.
    # It's automatically called when you create a new object (instance) of the class.
    # 'self' is a reference to the current object being created. It's always the first parameter.
    # make, model, and year are parameters that define the attributes (characteristics) of a car.
    def __init__(self, make, model, year):
        # These lines assign the values passed as arguments to the object's attributes.
        # self.make means "the make of this specific car object".
        self.make = make  # Assigns the provided make to the car's make attribute.
        self.model = model # Assigns the provided model to the car's model attribute.
        self.year = year  # Assigns the provided year to the car's year attribute.

    # This is a method (a function within a class) called update_year.
    # It's designed to change the year of a car object.
    # 'self' is again a reference to the specific car object whose year we want to update.
    # new_year is the new year value that we want to set.
    def update_year(self, new_year):
        self.year = new_year # Updates the car's year attribute with the new value.

    # This method displays information about the car in a user-friendly format.
    # It uses an f-string (formatted string literal) to create the output string.
    def display_info(self):
        return f"{self.year} {self.make} {self.model}" # Returns a formatted string with the car's year, make, and model.

# Creating an instance (object) of the Car class.
# This is like using the cookie cutter to make a cookie.
# We're creating a specific car with the make "Toyota", model "Corolla", and year 2020.
# my_car is a variable that now holds this specific car object.
my_car = Car("Toyota", "Corolla", 2020)

# Calling methods on the my_car object.
# This is like telling the cookie to do something.

# Calling the display_info method to get information about the car and printing it to the console.
print(my_car.display_info())
# Expected Output: "2020 Toyota Corolla"

# Calling the update_year method to change the year of the car to 2022.
my_car.update_year(2022)

# Calling display_info again to show the updated information.
print(my_car.display_info())
# Expected Output: "2022 Toyota Corolla"

#Key takeaways:
# - A class is a template for creating objects.
# - Objects have attributes (data) and methods (actions).
# - __init__ is a special method that sets up the object's initial state.
# - self refers to the current object.
# - Methods are functions defined inside a class.