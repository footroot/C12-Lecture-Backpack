# Product class: Represents an individual product in the cart
class Product:
    """
    A class that represents a product with a name and price.
    Includes methods for comparison, string representation, and price calculation.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.

    Methods:
        __str__(): Returns a user-friendly string representation of the product.
        __repr__(): Returns a detailed string representation of the product for debugging.
        __lt__(other): Compares the product's price with another product's price.
        __add__(other): Adds the product's price with another product's price or a numeric value.
    """
    def __init__(self, name, price):
        """
        Initializes a Product instance with a name and price.

        Parameters:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns a user-friendly string representation of the product.

        Returns:
            str: A formatted string with the product's name and price.
        """
        return f"{self.name} (${self.price:.2f})"

    def __repr__(self):
        """
        Returns a string representation for debugging.

        Returns:
            str: A detailed string with the product's name and price.
        """
        return f"Product('{self.name}', {self.price})"

    def __lt__(self, other):
        """
        Compares the price of this product with another product's price.

        Parameters:
            other (Product): Another product to compare.

        Returns:
            bool: True if the price of this product is less than the other's price.
        """
        return self.price < other.price

    def __add__(self, other):
        """
        Adds the price of this product with another product's price or a numeric value.

        Parameters:
            other (Product, int, float): The product or numeric value to add.

        Returns:
            float: The result of adding the prices.
            or
            NotImplemented if the other object is not a valid type.
        """
        if isinstance(other, (int, float)):
            return self.price + other
        elif isinstance(other, Product):
            return self.price + other.price
        else:
            return NotImplemented

# Cart class: Represents a shopping cart that contains multiple products
class Cart:
    """
    A class that represents a shopping cart for a customer. The cart can contain multiple products.

    Attributes:
        customer_name (str): The name of the customer.
        items (list): A list of products in the cart.

    Methods:
        add_item(product): Adds a product to the cart.
        total(): Returns the total price of all products in the cart.
        __str__(): Returns a string representation of the cart, listing all products and the total.
        __len__(): Returns the number of items in the cart.
    """
    def __init__(self, customer_name):
        """
        Initializes a Cart instance for a specific customer.

        Parameters:
            customer_name (str): The name of the customer.
        """
        self.customer_name = customer_name
        self.items = []

    def add_item(self, product):
        """
        Adds a product to the cart.

        Parameters:
            product (Product): The product to add to the cart.
        """
        self.items.append(product)

    def total(self):
        """
        Calculates the total price of all items in the cart.

        Returns:
            float: The total price of all products in the cart.
        """
        return sum(item.price for item in self.items)

    def __str__(self):
        """
        Returns a string representation of the cart, including the customer’s name,
        the products in the cart, and the total price.

        Returns:
            str: A string summary of the cart.
        """
        receipt = f"Cart for {self.customer_name}:\n"
        for item in self.items:
            receipt += f" - {item}\n"
        receipt += f"Total: ${self.total():.2f}"
        return receipt

    def __len__(self):
        """
        Returns the number of products in the cart.

        Returns:
            int: The number of items in the cart.
        """
        return len(self.items)

# DiscountedProduct class: Represents a product with a discount applied
class DiscountedProduct:
    """
    A class that represents a discounted product. It does not inherit from the Product class.

    Attributes:
        name (str): The name of the product.
        price (float): The price after the discount is applied.

    Methods:
        __str__(): Returns a string representation of the discounted product.
        __repr__(): Returns a detailed string representation for debugging.
    """
    def __init__(self, name, price, discount):
        """
        Initializes a DiscountedProduct instance with a name, original price, and discount.

        Parameters:
            name (str): The name of the product.
            price (float): The original price of the product.
            discount (float): The discount rate (0.2 for 20% off).
        """
        self.name = name
        self.price = price * (1 - discount)

    def __str__(self):
        """
        Returns a string representation of the discounted product.

        Returns:
            str: A string with the discounted product's name and price.
        """
        return f"{self.name} (${self.price:.2f}) (Discounted)"

    def __repr__(self):
        """
        Returns a detailed string for debugging.

        Returns:
            str: A string with the discounted product's name and price.
        """
        return f"DiscountedProduct('{self.name}', {self.price})"

# DiscountedProduct class with Inheritance: Represents a discounted product with inheritance from Product
class DiscountedProduct(Product):
    """
    A subclass of Product that represents a product with a discount applied.

    This class overrides the __str__ and __repr__ methods to include discount information.
    
    Attributes:
        discount (float): The discount rate applied to the product.
    """
    def __init__(self, name, price, discount):
        """
        Initializes a DiscountedProduct instance with a name, original price, and discount.

        Parameters:
            name (str): The name of the product.
            price (float): The original price of the product.
            discount (float): The discount rate (0.2 for 20% off).
        """
        super().__init__(name, price)  # Initialize the base class
        self.discount = discount
        self.price = self.price * (1 - self.discount)

    def __str__(self):
        """
        Returns a string representation of the discounted product.

        Returns:
            str: A string with the discounted product's name and price.
        """
        return f"{self.name} (${self.price:.2f}) (Discounted)"

    def __repr__(self):
        """
        Returns a detailed string for debugging.

        Returns:
            str: A string with the discounted product's name and price.
        """
        return f"DiscountedProduct('{self.name}', {self.price})"


# Example usage of the above classes
apple = Product("Apple", 1.0)  # Creating a basic product
banana = Product("Banana", 0.5)  # Creating another product
milk = Product("Milk", 3.0)  # Creating another product
discounted_milk = DiscountedProduct("Milk", 3.0, 0.2)  # Creating a discounted product (20% off)

# Create a shopping cart for a customer
my_cart = Cart("Alice")
my_cart.add_item(apple)
my_cart.add_item(banana)
my_cart.add_item(discounted_milk)  # Adding a discounted product

# Print the cart and its details
print(my_cart)

# Print the length of the cart (number of items)
print(f"Cart Length: {len(my_cart)}")

# Use the comparison method to compare product prices
print(apple < milk)  # Check if apple is cheaper than milk

# Use the operator overloading method to add product prices
print(apple + banana)  # Add prices of apple and banana

print(apple > banana)  # Will raise an error since __lt__ is defined but not __gt__

# Example of type checking when adding items to the cart
try:
    my_cart.add_item("not a product")  # Trying to add an invalid item type
except TypeError as e:
    print(e)  # Catch the TypeError and print the message