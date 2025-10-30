# Basic Calculator with Error Handling
# This program demonstrates the use of try-except blocks, error handling, and input validation

def get_valid_number(prompt):
    """
    Function to get a valid number from user input
    Parameters:
        prompt (str): The message to show to the user
    Returns:
        float: The valid number entered by the user
    """
    while True:
        try:
            # Convert the input string to a float number
            number = float(input(prompt))
            return number
        except ValueError:
            # If user enters non-numeric value (like letters or special characters)
            print("Error: Please enter a valid number!")

def get_valid_operation():
    """
    Function to get a valid operation from user input
    Returns:
        str: The valid operation symbol (+, -, *, /)
    """
    while True:
        # Get operation from user
        operation = input("Choose an operation (+, -, *, /): ")
        
        # Check if the operation is valid
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            # If operation is not one of the valid symbols
            print("Error: Invalid operation! Please choose +, -, *, or /")

def perform_calculation(num1, num2, operation):
    """
    Function to perform the actual calculation
    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Mathematical operation to perform
    Returns:
        float: Result of the calculation
    """
    try:
        # Perform the calculation based on the operation
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            # Check for division by zero
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            return num1 / num2
            
    except ZeroDivisionError as e:
        # Handle division by zero error
        print(f"Error: {e}")
        return None

def calculator():
    """
    Main calculator function that runs the program
    """
    print("\n=== Welcome to the Basic Calculator ===\n")
    
    while True:
        try:
            # Get the first number
            num1 = get_valid_number("Enter the first number: ")
            
            # Get the second number
            num2 = get_valid_number("Enter the second number: ")
            
            # Get the operation
            operation = get_valid_operation()
            
            # Perform the calculation
            result = perform_calculation(num1, num2, operation)
            
            # Display the result if calculation was successful
            if result is not None:
                print(f"\nResult: {num1} {operation} {num2} = {result}")
            
            # Ask if user wants to perform another calculation
            again = input("\nDo you want to perform another calculation? (yes/no): ")
            if again.lower() != 'yes':
                print("\nThank you for using the calculator! Goodbye!")
                break
                
        except Exception as e:
            # Catch any unexpected errors
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

# Start the calculator program
if __name__ == "__main__":
    calculator()