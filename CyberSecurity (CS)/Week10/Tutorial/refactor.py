import time

def process_order(order_type, quantity):
    price = 0
    if order_type == "apple":
        price = 1.2
    elif order_type == "banana":
        price = 0.8
    elif order_type == "orange":
        price = 1.5
    
    if quantity > 10:
        price *= 0.9

    total = price * quantity
    print("Processing order...")
    time.sleep(2)
    print(f"Order confirmed: {quantity} {order_type}(s) for ${total:.2f}")

def main():
    print("Welcome to the Fruit Store!")
    fruit = input("Enter fruit name (apple, banana, orange): ")
    qty = int(input("Enter quantity: "))

    if fruit == "apple" or fruit == "banana" or fruit == "orange":
        process_order(fruit, qty)
    else:
        print("Invalid fruit!")

main()
