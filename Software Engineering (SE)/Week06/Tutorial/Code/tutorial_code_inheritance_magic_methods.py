# 1. Basic Inheritance
class Property:
    """
    Represents a general property with a location and price.
    
    Attributes:
        location (str): The location of the property.
        price (float): The price of the property in USD.
    """
    def __init__(self, location, price):
        """
        Initializes a Property instance with location and price.
        
        Args:
            location (str): The location of the property.
            price (float): The price of the property in USD.
        """
        self.location = location
        self.price = price

    def show_details(self):
        """
        Displays details of the property.
        
        Returns:
            str: A string representation of the property's location and price.
        """
        return f"Location: {self.location}, Price: {self.price} USD"

    def __repr__(self):
        """
        Provides a developer-friendly string representation of the Property.
        
        Returns:
            str: The representation of the property instance.
        """
        return f"Property({self.location}, {self.price} USD)"

    def __eq__(self, other):
        """
        Compares two properties for equality based on price.
        
        Args:
            other (Property): Another property to compare with.
        
        Returns:
            bool: True if prices are equal, False otherwise.
        """
        return self.price == other.price

    def __lt__(self, other):
        """
        Compares two properties to determine if one is less expensive.
        
        Args:
            other (Property): Another property to compare with.
        
        Returns:
            bool: True if this property is cheaper, False otherwise.
        """
        return self.price < other.price

    def __add__(self, other):
        """
        Adds the prices of two properties.
        
        Args:
            other (Property): Another property to add prices with.
        
        Returns:
            float: The sum of the two property prices.
        """
        return self.price + other.price


# Derived Class
class Apartment(Property):
    """
    Represents an Apartment, inheriting from Property.
    """
    pass

# Usage of the basic inheritance
apartment = Apartment("Downtown", 120000)
print(apartment.show_details())  # Outputs: Location: Downtown, Price: 120000 USD

####################################################################
# 2. Change the Behaviour of a Subclass

class Apartment(Property):
    """
    Represents an Apartment with additional floor information.
    """
    def __init__(self, location, price, floor):
        """
        Initializes an Apartment with location, price, and floor details.
        
        Args:
            location (str): The location of the apartment.
            price (float): The price of the apartment in USD.
            floor (int): The floor number where the apartment is located.
        """
        # Using super() ensures we correctly call the initializer of the parent class (Property),
        # avoiding manually specifying the parent class. This improves maintainability.
        super().__init__(location, price)
        self.floor = floor

    def show_details(self):
        """
        Displays details specific to the apartment.
        
        Returns:
            str: Details of the apartment, including the floor.
        """
        # Using super().show_details() calls the parent class's method
        # and appends additional information about the floor.
        return f"Apartment on Floor: {self.floor}, " + super().show_details()

# Usage
apartment = Apartment("Uptown", 100000, 5)
print(apartment.show_details())  # Outputs: Apartment on Floor: 5, Location: Uptown, Price: 100000 USD


class House(Property):
    """
    Represents a House with an additional garden size attribute.
    """
    def __init__(self, location, price, garden_size):
        """
        Initializes a House with location, price, and garden size details.
        
        Args:
            location (str): The location of the house.
            price (float): The price of the house in USD.
            garden_size (float): The size of the garden in square meters.
        """
        # super() ensures we use the initializer of Property to avoid code duplication.
        super().__init__(location, price)
        self.garden_size = garden_size

    def show_details(self):
        """
        Displays details specific to the house.
        
        Returns:
            str: Details of the house, including the garden size.
        """
        # Combining the details from the parent class (Property) with garden size.
        return super().show_details() + f", Garden Size: {self.garden_size} sqm"

# Usage
house = House("Suburbs", 250000, 300)
print(house.show_details())  # Outputs: Location: Suburbs, Price: 250000 USD, Garden Size: 300 sqm

####################################################################
# 3. Introducing super()

# In the House class above, `super()` is used to:
# 1. Call the initializer of the parent class (`Property`) to set common attributes like `location` and `price`.
# 2. Reuse the `show_details()` method from the parent class and extend it with subclass-specific details (`garden_size`).

####################################################################
# 4. Multiple Inheritance

class CommercialSpace(Property):
    """
    Represents a Commercial Space, inheriting from Property.
    """
    def __init__(self, location, price, business_type):
        """
        Initializes a Commercial Space with additional business type information.
        
        Args:
            location (str): The location of the commercial space.
            price (float): The price of the commercial space in USD.
            business_type (str): The type of business the space is suited for.
        """
        super().__init__(location, price)
        self.business_type = business_type

class Parking:
    """
    Represents a parking feature with a specified number of slots.
    """
    def __init__(self, parking_slots):
        """
        Initializes parking with the number of available slots.
        
        Args:
            parking_slots (int): Number of parking slots available.
        """
        self.parking_slots = parking_slots

class CommercialWithParking(CommercialSpace, Parking):
    """
    Represents a Commercial Space with parking facilities, inheriting from both
    CommercialSpace and Parking classes.
    """
    def __init__(self, location, price, business_type, parking_slots):
        """
        Initializes a Commercial Space with parking slots and business type.
        
        Args:
            location (str): Location of the commercial space.
            price (float): Price of the commercial space in USD.
            business_type (str): Type of business the space is suited for.
            parking_slots (int): Number of parking slots available.
        """
        # Explicitly initializing both parent classes to handle attributes from both hierarchies.
        CommercialSpace.__init__(self, location, price, business_type)
        Parking.__init__(self, parking_slots)

    def show_details(self):
        """
        Displays details of the commercial space including parking slots.
        
        Returns:
            str: Details of the commercial space and parking.
        """
        # super() calls the CommercialSpace implementation of show_details()
        # and appends parking-specific details from Parking.
        return (super().show_details() +
                f", Business Type: {self.business_type}, Parking Slots: {self.parking_slots}")

# Usage
commercial = CommercialWithParking("Business District", 500000, "Retail", 50)
print(commercial.show_details())  # Outputs: Location: Business District, Price: 500000 USD, Business Type: Retail, Parking Slots: 50

####################################################################
# 5. Special Methods

# Demonstrates the usage of special methods (__repr__, __eq__, __lt__, __add__).

print(house)  # Uses __repr__: Property(Suburbs, 250000 USD)
print(apartment)  # Uses __repr__: Property(Uptown, 100000 USD)
print(house == commercial)  # Uses __eq__: False
print(commercial < house)  # Uses __lt__: False
print(house + apartment)  # Uses __add__: 350000
