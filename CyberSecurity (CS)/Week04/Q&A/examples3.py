import csv

# Open the CSV file in read mode
with open("files\\examples.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings

import csv

# Open the CSV file
with open("files\\examples.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is a dictionary with column names as keys


import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Open the CSV file in write mode
with open("files\\output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once


import pandas as pd

# Reading a CSV file
df = pd.read_csv("files\\examples.csv")
print(df)
for line in df:
    print(line)

# Writing to a CSV file
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write to a CSV file
df.to_csv("output.csv", index=False)


# provide link to further learn pandas