import pandas as pd
import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define dataset size
num_records = 3900

# Helper functions for generating data


def random_choice(options, size):
    return [random.choice(options) for _ in range(size)]


def random_numeric_range(low, high, size, precision=2):
    return [round(random.uniform(low, high), precision) for _ in range(size)]


# Generate data columns
data = {
    "Customer ID": [f"CUST{1000 + i}" for i in range(num_records)],
    "Age": random_numeric_range(18, 70, num_records),
    "Gender": random_choice(["Male", "Female"], num_records),
    "Item Purchased": random_choice(
        ["T-shirt", "Laptop", "Shoes", "Book",
            "Headphones", "Smartphone", "Bag"], num_records
    ),
    "Category": random_choice(
        ["Apparel", "Electronics", "Footwear", "Books", "Accessories"], num_records
    ),
    "Purchase Amount (USD)": random_numeric_range(5, 1000, num_records),
    "Location": random_choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"], num_records),
    "Size": random_choice(["S", "M", "L", "XL"], num_records),
    "Color": random_choice(["Red", "Blue", "Black", "White", "Green"], num_records),
    "Season": random_choice(["Winter", "Spring", "Summer", "Fall"], num_records),
    "Review Rating": random_numeric_range(1, 5, num_records, precision=1),
    "Subscription Status": random_choice(["Yes", "No"], num_records),
    "Shipping Type": random_choice(["Standard", "Express", "Overnight"], num_records),
    "Discount Applied": random_choice(["Yes", "No"], num_records),
    "Promo Code Used": random_choice(["Yes", "No"], num_records),
    "Previous Purchases": random_numeric_range(0, 50, num_records, precision=0),
    "Payment Method": random_choice(["Credit Card", "Debit Card", "PayPal", "Cash"], num_records),
    "Frequency of Purchases": random_choice(["Weekly", "Monthly", "Quarterly"], num_records),
}

# Define columns where missing values will be added
columns_with_missing_values = [
    'Purchase Amount (USD)', 'Review Rating', 'Payment Method']


# Create DataFrame
customer_data = pd.DataFrame(data)

# Add missing values randomly (approximately 10% of rows for the specified columns)
for column in columns_with_missing_values:
    data.loc[data.sample(frac=0.1, random_state=42).index, column] = np.nan

# Verify if missing values have been added
data.isnull().sum()

# Save to CSV for use
file_path = "/mnt/data/customer_shopping_preferences.csv"
customer_data.to_csv(file_path, index=False)

file_path
