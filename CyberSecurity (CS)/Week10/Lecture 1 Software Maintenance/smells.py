from placeholders import email_service, logging

# Long Method
def validate_order(order):
    if not order.is_valid():
        raise ValueError("Invalid order")
    
def calculate_total(order):
    return sum(item.price * item.quantity for item in order.items)

def apply_discount(total, customer):
    return total * 0.9 if customer.is_premium() else total

def process_order(order):
    validate_order(order)
    total = calculate_total(order)
    total = apply_discount(total, order.customer)
    order.total = total
    order.save()
    email_service.send_confirmation(order.customer.email, order)
    logging.info(f"Order processed: {order.id}")


# Duplicate Code
def calculate_area_of_rectangle(width, length):
    return width * length

def calculate_area_of_square(side):
    return side * side

def calculate_area(length, width=None):
    return length * (width if width else length)

calculate_area(5)
calculate_area(11, 7)











# Large Class
class Order:
    def __init__(self, nr, items):
        self.nr = nr
        self.items = items
        self.status = "New"

class PricingService:
    @staticmethod
    def calculate_total(self):
        return sum(item.price for item in self.items)
    
    @staticmethod
    def apply_discount(self):
        total = self.calculate_total()
        return total * 0.1 if total > 100 else 0

class InvoiceService:
    def generate_invoice(self):
        print(f"Generating invoice for order {self.nr}")

class NotificationService:
    @staticmethod
    def send_email_confirmation(self):
        print(f"Sending email for order {self.nr}")

# Lazy class
class Order:
    def calculate_discount(self):
        return 0.0



# Feature Envy
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def print_address(self):
        print(f"Customer Address: {self.address}")




# Temporary Fields
class Order:
    def __init__(self, customer):
        self.customer = customer

    def apply_discount(self, discount_code):
        pass












# Excessive Comments
def add_numbers(a, b):
    """"""
    return a + b

def main():
    num1 = 5
    num2 = 10
    result = add_numbers(num1, num2)
    print("The sum is:", result)

if __name__ == "__main__":
    main()