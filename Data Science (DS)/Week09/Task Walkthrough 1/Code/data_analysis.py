# Create our functions: read the csv, filter, calculate total, generate report

# 1. Read csv file
def read_sales_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()  # Read all lines into a list
    
    headers = lines[0].strip().split(",")  # Extract column headers
    sales_data = []  # List to store processed sales records

    # Process each transaction (skipping the header row)
    for line in lines[1:]:
        values = line.strip().split(",")  # Split row into values

        record = {}
        for i in range(len(headers)):
            record[headers[i]] = values[i]
           
        # Convert numerical fields
        record["Quantity"] = int(record["Quantity"])
        record["Price per Unit"] = float(record["Price per Unit"])
        record["Total Amount"] = record["Quantity"] * record["Price per Unit"]  # Compute total sale

        sales_data.append(record)  # Add to list
    
    return sales_data

# 2. Filter transactions above a threshold
def filter_high_value_transactions(sales, threshold=100):
    results = []
    for sale in sales:
        if sale["Total Amount"] > threshold:
            results.append(sale)

    return results

# 3. Calculate total amount spent per customer
def total_sales_per_customer(sales):
    customer_totals = {}
    for sale in sales:
        customer_id = sale["Customer ID"]
        customer_totals[customer_id] = customer_totals.get(customer_id, 0) + sale["Total Amount"]
    return customer_totals

# 4. Generate final insights report, write to file
def write_summary_to_file(summary, filename="sales_summary.txt"):
    with open(filename, 'w') as file:
        for customer, total in summary.items():
            file.write(f"Customer {customer}: ￡{total:.2f}\n")


if (__name__ == "__main__"):
    sales_data = read_sales_data("sales.csv")
    filtered_sales = filter_high_value_transactions(sales_data, 300)
    sales_summary = total_sales_per_customer(filtered_sales)
    write_summary_to_file(sales_summary)

    print("Sales data processed and summary saved!")