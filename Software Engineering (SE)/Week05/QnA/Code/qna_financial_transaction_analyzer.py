from functools import reduce

def log_transaction(func):
   def wrapper(*args):
       result = func(*args)
       print(f"Transaction added: {args[1:]}")
       return result
   return wrapper

class TransactionAnalyzer:
    number_of_transactions = 0

    def __init__(self):
        self.transactions = []

    @log_transaction
    def add_transaction(self, date, description, amount):
        self.transactions.append((date, description, amount))
        TransactionAnalyzer.update_number_of_transactions()

    def calculate_balance(self):
        return reduce(lambda acc, txn: acc + txn[2], self.transactions, 0)

    def filter_transactions(self, condition):
        return list(filter(condition, self.transactions))

    @staticmethod
    def convert_usd_to_pounds(amount_in_usd, exchange_rate=1.25):
        return amount_in_usd * exchange_rate

    def convert_all_transactions(self, exchange_rate=0.85):
        converted_transactions = list(map(
            lambda txn: (txn[0], txn[1], self.convert_usd_to_pounds(txn[2], exchange_rate)), 
            self.transactions
        ))
        return converted_transactions

    @classmethod
    def update_number_of_transactions(cls):
        cls.number_of_transactions += 1

    @classmethod
    def get_number_of_transactions(cls):
        return cls.number_of_transactions
    
    def read_transactions_from_file(self, filename):
        try:
            # Open the file for reading
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()  # Remove any extra spaces or newline characters
                    parts = line.split(",")  # Split the line by commas
                    
                    # Ensure the line has exactly 3 parts: date, description, amount
                    if len(parts) != 3:
                        print(f"Skipping invalid line: {line}. Expected 3 comma-separated values.")
                        continue
                    
                    try:
                        # Add the transaction if it's valid
                        self.add_transaction(parts[0], parts[1], float(parts[2]))
                    except ValueError as e:
                        # Handle any errors that occur while converting amount to float
                        print(f"Error processing line: {line}. {e}")
        except FileNotFoundError:
            # Handle the case where the file is not found
            print(f"Error: File '{filename}' not found.")
            return None
        return None

# Example Usage
if __name__ == "__main__":
    # Create an instance of TransactionAnalyzer
    analyzer = TransactionAnalyzer()

    # Add some transactions manually: Add one first, then switch to file reading.
    analyzer.add_transaction("2024-12-31", "Coffee Shop", -5.50)
    analyzer.add_transaction("2025-01-01", "Coffee Shop", -5.50)
    analyzer.add_transaction("2025-01-02", "Salary", 2000.00)
    analyzer.add_transaction("2025-01-03", "Rent", -750.00)

    # # Uncomment to read transactions from a file (e.g., "transactions.txt")
    # analyzer.read_transactions_from_file("transactions.txt")

    print(f"Number of transactions: {analyzer.get_number_of_transactions()}")

    # Calculate and display total balance in both currencies
    balance = analyzer.calculate_balance()
    balance_pound = TransactionAnalyzer.convert_usd_to_pounds(balance)
    print(f"Total balance: ${balance:.2f}. It's equivalent to £{balance_pound} \n")

    # Filter expenses and convert to GBP
    expenses = analyzer.filter_transactions(lambda t: t[2] < 0)
    expenses = analyzer.convert_all_transactions()

    print("Expenses in GBP:")
    for txn in expenses:
        print(f"{txn[0]} - {txn[1]}: £{txn[2]:.2f}")