def my_function(parameter1, parameter2):
    # Do something with input data AKA parameters.
    return # output


def add_values(num1, num2):
    return num1 + num2


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def draw_line(symbol="-", length=80):
    return symbol * length + "\n"


def student_card(name, surname, course, student_id):
    card = draw_line(length=25)
    card += f"Name:\t\t{name}\nSurname:\t{surname}\nCourse:\t\t{course}\nID:\t\t{student_id}\n"
    card += draw_line(length=25)
    return card

print(student_card("Jane", "Peterson", "CS", "12345"))

# Students challenge
# Create a function that takes a string as an argument and
# returns the reverse of that string.
def reverse_str(text):
    return text[::-1]

def reverse_str(text):
    new_str = ""
    for char in text:
        new_str = char + new_str
    return new_str

# Create a function that take a integer value and returns
# true if the value is even and false if the value is not.
def is_even(num):
    return num % 2 == 0


# installing 3rd party packages
from tabulate import tabulate

movies = [
    ["Inception", 148, "Sci-Fi"],
    ["The Dark Knight", 152, "Action"],
    ["Forrest Gump", 142, "Drama"],
    ["The Lion King", 88, "Animation"],
    ["Avengers: Endgame", 181, "Superhero"],
    ["The Shawshank Redemption", 142, "Drama"],
    ["Pulp Fiction", 154, "Crime"],
    ["The Matrix", 136, "Sci-Fi"],
    ["Frozen", 102, "Animation"],
    ["Interstellar", 169, "Sci-Fi"]
]
headers = ["Movie", "Runtime", "Genre"]

print(tabulate(movies, headers=headers))

# Lambda functions
# Small anonymous function
equal = lambda x, y: x == y
print(equal(1,2))
print(equal(3,3))


# Multiple returns
def divide_numbers(a, b):
    if b == 0:
        return False, "Division by zero is not allowed!"
    return True, a / b

status, result = divide_numbers(10, 0)
if status:
    print("Result:", result)
else:
    print("Error:", result)
