"""
Title: ATM Simulator

Objective:
This program simulates an ATM process. Customers can withdraw or deposit money based on their available balance. The program ensures:
- Valid input for withdrawal and deposit amounts.
- Error handling for insufficient funds, large deposits, and invalid input.
- A deposit threshold to prevent excessively large deposits.
- Logging of all transactions (successful or failed) to a file with timestamps.
"""

import datetime  # Module to get the current date and time for transaction logs.

# Initial customer balance
current_balance = 10000  # The starting balance for the customer.
deposit_threshold = 1000000  # The maximum allowed deposit amount.
log_file_name = "transactions_logs.txt"  # The name of the file where transaction logs will be stored.

# Define a custom exception for insufficient funds.
class InsufficientFundsError(Exception):
    """Custom exception to handle cases where the withdrawal amount exceeds the balance."""
    pass  # Placeholder for this exception. It doesn't need additional functionality here.

def file_operations(message, file_name=log_file_name, access_mode='a'):
    """
    Logs messages to a file with a timestamp and displays them on the screen.

    Args:
        message (str): The message to log.
        file_name (str): The name of the log file.
        access_mode (str): The mode to open the file ('a' for append by default).

    This function adds a timestamp to each message, writes it to the file, 
    and prints it to the screen.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp.
    log_message = f"[{timestamp}] {message}\n"  # Format the message with the timestamp.
    with open(file_name, access_mode) as file:  # Open the file in append mode.
        file.write(log_message)  # Write the log message to the file.
    print(log_message, end="")  # Print the message without adding an extra newline.

def handle_withdrawal(user_s_balance, amount):
    """
    Handles the withdrawal process, ensuring the amount is valid.

    Args:
        user_s_balance (float): The current balance of the user.
        amount (float): The amount to withdraw.

    Returns:
        float: The updated balance after withdrawal.

    This function raises an InsufficientFundsError if the withdrawal amount 
    exceeds the available balance.
    """
    file_operations(f"The user attempted to withdraw {amount}.")  # Log the attempted withdrawal.
    if amount > user_s_balance:  # Check if the amount exceeds the balance.
        error_message = "You don't have enough money to withdraw this amount."
        file_operations(f"Error Message: {error_message}")
        raise InsufficientFundsError("Insufficient balance for this transaction.")  # Raise a custom exception.
    user_s_balance -= amount  # Deduct the withdrawal amount from the balance.
    file_operations(f"New balance after withdrawal is: {user_s_balance}")  # Log the new balance.
    return user_s_balance  # Return the updated balance.

def handle_deposit(user_s_balance, amount, deposit_threshold=deposit_threshold):
    """
    Handles the deposit process, ensuring the amount is valid.

    Args:
        user_s_balance (float): The current balance of the user.
        amount (float): The amount to deposit.
        deposit_threshold (float): The maximum allowed deposit amount.

    Returns:
        float: The updated balance after deposit.

    This function raises an OverflowError if the deposit amount is excessively large.
    """
    file_operations(f"The user attempted to deposit {amount}.")  # Log the attempted deposit.
    if amount > deposit_threshold:  # Check if the deposit exceeds the threshold.
        # Inform the user that the deposit amount is too large.
        file_operations(f"Error: Deposit exceeds the threshold of {deposit_threshold}.")
        raise OverflowError("Deposit amount is too large. Please reduce the amount.")  # Raise a custom exception.
    user_s_balance += amount  # Add the deposit amount to the balance.
    file_operations(f"New balance after deposit is: {user_s_balance}")  # Log the new balance.
    return user_s_balance  # Return the updated balance.

def main_process(user_s_balance):
    """
    The main function to handle user interactions and perform transactions.

    Args:
        user_s_balance (float): The current balance of the user.

    Returns:
        float: The final balance after all transactions.
    """
    while True:  # Run the ATM process in a loop until the user chooses to exit.
        try:
            # Ask the user for their desired action.
            deposit_withdraw_decision = input("Would you like to withdraw (0), deposit (1) money, or cancel (2)? : ")

            if deposit_withdraw_decision == '0':  # Withdrawal
                file_operations("The user chose operation: Withdrawal.")
                amount = float(input("Enter the amount to withdraw: "))
                user_s_balance = handle_withdrawal(user_s_balance, amount)  # Call the withdrawal function.

            elif deposit_withdraw_decision == '1':  # Deposit
                file_operations("The user chose operation: Deposit.")
                amount = float(input("Enter the amount to deposit: "))
                user_s_balance = handle_deposit(user_s_balance, amount, deposit_threshold)  # Call the deposit function.

            elif deposit_withdraw_decision == '2':  # Exit
                file_operations("Have a great day!")  # Log the exit message.
                break  # Exit the loop.

            else:  # Invalid input
                file_operations("Error: Invalid option! Please enter '0', '1', or '2'.")  # Log the error.

        except InsufficientFundsError as ei:  # Handle insufficient funds error.
            file_operations(f"Error encountered: {ei}")
            file_operations("Please try again ... :)")

        except ValueError as ev:  # Handle invalid input (non-numeric).
            file_operations(f"Error encountered: {ev}")
            file_operations("Invalid input! Please enter a valid number.")

        except OverflowError as eo:  # Handle excessively large deposits.
            file_operations(f"Error encountered: {eo}")
            file_operations("Please try again with a smaller amount.")
         finally:
            # Ensure this block executes no matter what happens
            file_operations("Transaction attempt concluded.")  # Log the end of the transaction attempt.

    return user_s_balance  # Return the updated balance after all transactions.

# Entry point of the program
if __name__ == "__main__":
    file_operations("Welcome to the Bank!")  # Welcome message.
    file_operations(f"Your current balance is: {current_balance}")  # Display the initial balance.
    current_balance = main_process(current_balance)  # Start the main process and update the balance.
    file_operations(f"Your final balance is: {current_balance}")  # Display the final balance.
