# Let's assume that we have a list of people and we want to:
# - get people who have older than 18 years old. 
# - calculate their number of years to retirement
# - print their retirement age
# - Get the average of age of the people who are older than 18 years old
# The aim is to implement the same functionality using plain functions, higher order functions and decorators.

# List of people with their ages
people = [12, 38, 7, 19, 43, 23, 11, 20, 18, 10, 5, 8, 30, 49]


###################################################################################################################################################################################

print("This section is for plain functions\n")

# Just Using plain functions

# Get people who have older than 18 years old
def get_people_older_than_18(people):
    """Get people who have older than 18 years old
    Args:
        people (list): List of people with their ages
    Returns:
        list: List of people who are older than 18 years old
    """
    people_older_than_18 = []
    for person in people:
        if person > 18:
            people_older_than_18.append(person)
    return people_older_than_18

people_older_than_18 = get_people_older_than_18(people)
print(f"People who are older than 18 years old: {people_older_than_18}")

# Calculate their retirement age
def calculate_retirement_years(people_older_than_18):
    """Calculate their retirement age
    Args:
        people_older_than_18 (list): List of people who are older than 18 years old
    Returns:
        list: List of years to retirement for each person
    """
    retirement_age = 65
    retirement_years = []
    for person in people_older_than_18:
        person_retirement_years = 0
        person_retirement_years = retirement_age - person
        retirement_years.append(person_retirement_years)
    return retirement_years
            
retirement_ages = calculate_retirement_years(people_older_than_18)
print(f"Years to retirement: {retirement_ages}")

# Get the average of age of the people who are older than 18 years old
def get_average_age(people_older_than_18):
    """Get the average of age of the people who are older than 18 years old
    Args:
        people_older_than_18 (list): List of people who are older than 18 years old
    Returns:
        float: Average age of people who are older than 18 years old
    """
    total_age = 0
    for person in people_older_than_18:
        total_age += person
    return total_age / len(people_older_than_18)

average_age = get_average_age(people_older_than_18)
print(f"Average age of people who are older than 18 years old: {average_age}")

print("\n")
###################################################################################################################################################################################

print("This section is for higher order functions: map, reduce, filter\n")

# Just Using Higher Order Functions

# Using filter and lambda functions, get people who have older than 18 years old

def get_people_older_than_18_filter(list_of_people):
    people_older_than_18 = list(filter(lambda x: x > 18, list_of_people))
    return people_older_than_18

people_older_than_18_filter = get_people_older_than_18_filter(people)
print(f"Filter - People who are older than 18 years old: {people_older_than_18_filter}")

# Using map and lambda functions, calculate their retirement age
def calculate_retirement_years_map(people_older_than_18):
    retirement_age = 65
    retirement_years = list(map(lambda x: retirement_age - x, people_older_than_18))
    return retirement_years

retirement_ages = calculate_retirement_years_map(people)
print(f"Map - Years to retirement using map: {retirement_ages}")

# Using reduce and lambda functions, get the average of age of the people who are older than 18 years old
from functools import reduce

def average_age_people(people):
    average_age = reduce(lambda x, y: x + y, people) / len(people)
    return average_age
print(f"Reduce - Average age of people who are older than 18 years old: {average_age}")

print("\n")
###################################################################################################################################################################################

print("This section is for decorators\n")

# Just Using decorators

# Now let's assume that we would to instanly calculate people number of years to retirements and the average of their age.
# We need to make sure that the people should be older than 18

# funcdamentals of decorators
def filter_underaged_basic(func, people):
    people_older_than_18 = list(filter(lambda x: x > 18, people))
    return func(people_older_than_18)

# Only get people who have older than 18 years old
def filter_underaged(func):
    def wrapper(people):
        people_older_than_18 = list(filter(lambda x: x > 18, people))
        return func(people_older_than_18)
    return wrapper

@filter_underaged
def get_years_to_retirement(people):
    retirement_age = 65
    retirement_years = list(map(lambda x: retirement_age - x, people))
    return retirement_years

@filter_underaged
def print_people(people):
    return people

people_all = print_people(people)
print(f"This is the initial list: {people_all}")        

@filter_underaged
def calculate_retirement_years_map(people_older_than_18):
    retirement_age = 65
    retirement_years = list(map(lambda x: retirement_age - x, people_older_than_18))
    return retirement_years

retirement_ages = calculate_retirement_years_map(people)
print(f"Years to retirement using map: {retirement_ages}")

from functools import reduce
@filter_underaged
def average_age_people(people):
    average_age = reduce(lambda x, y: x + y, people) / len(people)
    return average_age

print(f"Average age of people who are older than 18 years old: {average_age_people(people)}")