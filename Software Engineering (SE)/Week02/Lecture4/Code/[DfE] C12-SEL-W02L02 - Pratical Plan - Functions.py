# Take two numbers as input, convert them to floats, and add them
num1 = float(input("Enter first number: "))  # Prompt for the first number
num2 = float(input("Enter second number: "))  # Prompt for the second number
result = num1 + num2  # Add the two numbers
print(f"{num1} + {num2} = {result}")  # Display the result

# Take two numbers as input, convert them to floats, and subtract them
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 - num2  # Subtract the second number from the first
print(f"{num1} - {num2} = {result}")

# Take two numbers as input, convert them to floats, and multiply them
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 * num2  # Multiply the two numbers
print(f"{num1} * {num2} = {result}")

# Take two numbers as input, convert them to floats, and divide them
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num2 == 0:  # Check if the second number is zero
    print("Error! Division by zero.")  # Display error for division by zero
else:
    result = num1 / num2  # Divide the first number by the second
    print(f"{num1} / {num2} = {result}")  # Display the result

# Define a function to add two integers
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    """
    return a + b

# Define a function to multiply two integers
def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers and returns the result.
    """
    return a * b

# Define a function to subtract two integers
def subtract(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first and returns the result.
    """
    return a - b

# Define a function to divide two integers
def divide(a: int, b: int) -> float:
    """
    Divides the first integer by the second and returns the result.
    """
    if b == 0:  # Check if the denominator is zero
        return "Error! Division by zero."
    return a / b  # Perform division

# Define a function to greet a person with a message
def greet(name: str, message: str = "Hello") -> str:
    """
    Greets a person with a specified message.
    """
    return f"{message}, {name}!"

# Example usage of the greet function
print(greet("Alice"))  # Greet using the default message
print(greet(name="Bob", message="Hi"))  # Greet with a custom message
print(greet(message="Welcome", name="Charlie"))  # Demonstrate flexible argument order

# Demonstrate usage of a global variable
global_var = 10

def read_global():
    """
    Reads and prints the value of a global variable.
    """
    print(global_var)  # Read the global variable

def modify_global():
    """
    Modifies the value of a global variable.
    """
    global global_var
    global_var = 20  # Modify the global variable

def try_modify_without_global():
    """
    Demonstrates creating a local variable with the same name as a global variable.
    """
    global_var = 30  # Create a local variable (does not affect the global)
    print(global_var)

read_global()  # Output: 10
modify_global()  # Modify the global variable
read_global()  # Output: 20
try_modify_without_global()  # Output: 30
read_global()  # Output: 20

# Define a simple calculator using the defined functions
def calculator():
    """
    A simple calculator that performs basic arithmetic operations based on user input.
    
    Operations include addition, subtraction, multiplication, and division.
    """
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")  # Get user choice for operation

    num1 = float(input("Enter first number: "))  # Get the first number
    num2 = float(input("Enter second number: "))  # Get the second number

    # Perform the operation based on user choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")  # Handle invalid user input

# Call the calculator function
calculator()
