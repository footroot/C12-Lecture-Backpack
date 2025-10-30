# Step 1: Planning
# Goal: Create a Basic Calculator program to perform simple arithmetic operations.
# Purpose: The program will allow users to perform addition, subtraction, multiplication, and division of two numbers.

# Step 2: Requirements Analysis
# Requirements:
# - The user can:
#   1. Select an operation (add, subtract, multiply, divide).
#   2. Input two numbers.
#   3. Get the result of the operation.
#   4. Exit the application.
# - The program should handle invalid inputs gracefully.

# Step 3: System Design
# Design:
# - Define functions for each arithmetic operation.
# - Implement a menu-driven interface to choose an operation.
#   - Basic Calculator Menu:
#     1. Add
#     2. Subtract
#     3. Multiply
#     4. Divide
#     0. Exit
# - Use input validation to ensure correct inputs.


# Step 4: Implementation (Coding)
# Implement the system based on the design.
MENU = """Basic Calculator Menu:
1. Add
2. Subtract
3. Multiply
4. Divide

0. Exit"""

while True:
    # Display menu
    print(MENU)
    
    # Get user choice
    choice = input("Enter your choice: ")

    if choice in {"1", "2", "3", "4"}:
        # Get input numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform the chosen operation
        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
            else:
                result = None
        print("-"*40)
        print(f"The result is: {result}")
        print("-"*40)
        input("Press enter to continue...")
    elif choice == "0":
        # Exit the application
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Step 5: Testing
# Test Cases:
# 1. Perform valid operations (e.g., addition of 3 and 5 should return 8).
# 2. Test division by zero (should display an error message).
# 3. Input invalid numbers (e.g., letters) and verify error handling.
# 4. Exit the application and ensure no errors occur.

# Step 6: Deployment
# To deploy:
# - Save the program to a `.py` file.
# - Run it in a Python environment or share it with users.

# Step 7: Maintenance
# Future Enhancements:
# - Add more operations (e.g., exponentiation, modulus).
# - Allow continuous calculations without returning to the menu.

