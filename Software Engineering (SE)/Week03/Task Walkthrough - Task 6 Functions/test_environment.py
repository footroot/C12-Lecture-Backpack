# 1. Create program to collect a random
# number of integers from the user.
# 2. Verify each value entered as an integer
# 3. Calculate the average of all the numbers.

# PEP8 guidelines for functions:
# 1. Double blank lines before and after.
# 2. Unique parameter names.
# 3. return values for testing purposes.

# Additional resources:
# __name__ parameter -> https://realpython.com/python-main-function/
# dictionary refresher -> https://www.geeksforgeeks.org/python-dictionary/
# try & except -> https://www.geeksforgeeks.org/python-try-except/

def collect_numbers():
    numbers = []
    next_number = True
    while next_number:
        number = validate_digit("Enter a number: ")
        if number == "x":
            next_number = False
        else:
            numbers.append(number)
    print(f"Average: {get_average(numbers)}")


def validate_digit(prompt: str) -> int:
    """
    Validates inputs as either 'x'
    or valid integers.

    :param prompt: input instruction.
    :return: string 'x' or valid integer.
    """
    while True:
        try:
            number = input(prompt)
            if number == "x":
                return number
            else:
                return int(number)
        except ValueError:
            print("Invalid number")


def get_average(numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        print("Nothing entered...")


if __name__ == "__main__":
    collect_numbers()

# BONUS CONTENT:
# Example of using a dictionary approach.
valid_flights = [
    "london",
    "new delhi",
    "tokyo"
]

flight_costs = {
    "london": 1200,
    "new delhi": 1500,
    "tokyo": 2400
}

while True:
    print(f"destinations: {valid_flights}")
    flight = input("Enter destination: ").lower()
    if flight in valid_flights:
        print(flight_costs[flight])
        