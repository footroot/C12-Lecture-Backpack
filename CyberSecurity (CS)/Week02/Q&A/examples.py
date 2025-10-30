# Basic If-statement
x = 10
if x > 5:
    print(f"{x} is larger than 5.")


# Temperature Check
temperature = int(input("Enter the temperature in degrees Celsius: "))

if temperature < 0:
    print("It's freezing!")
if temperature >= 0 and temperature <= 25:
    print("The weather is mild.")
if temperature > 25:
    print("It's hot!")


# Determine if a value is numeric before casting it to an int
value = input("Please enter a numeric value: ")
if value.isnumeric():
    value = int(value)
else:
    print("Non-numerical value entered.")


# Leap Year
# Cannot be divisible by 4
# Cannot be divisible by 100 unless also divisible by 400
year = int(input("Enter a year: "))

if not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("The year is NOT a leap year.")
else:
    print("The year is a leap year.")


# Short Circuiting
print("Checking 'and' short-circuiting:")

x = 5
y = 0

# Second condition is not checked because x < 10 is False
if x > 10 and y > 0:
    print("Both conditions are true.")
else:
    print("The first condition is false, so 'and' stops here.")

# Division by Zero
print("\nAvoiding division by zero:")

x = 5
y = 0

# Short-circuit prevents division by zero
if y != 0 and (x / y) > 1:
    print("Division result is greater than 1.")
else:
    print("Short-circuit prevents division by zero.")


# One value or the other.
print("\nProviding a default value:")

user_input = ""
default_value = "Guest"

# Short-circuit assigns a default value if user_input is empty
name = user_input or default_value
print(f"Hello, {name}!")


# Create an example menu that prompt a user to select an option.
# Allow the user to choose an option and show them the option they 
# have chosen. The program should then loop around and prompt another 
# option.
MENU = """MENU

1. Option 1
2. Option 2
3. Option 3

0. Exit"""
while True:
    print(MENU)
    option = input(": ")
    if option == "1":
        print("Option 1")
    elif option == "2":
        print("Option 2")
    elif option == "3":
        print("Option 3")
    elif option == "0":
        break


# For-loop reverse string
string = "Python is fun"
reversed_string = ""

for char in string:
    if char == " ":
        continue
    reversed_string = char + reversed_string

print(reversed_string)


# # Check Palindrome
word = ""
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

# Voting system
VOTE_MENU = """Please select a team to vote for:

A - Team 1
B - Team 2
C - Team 3
D - Team 4
: """

votes = int(input("Please enter the amount of voter allowed: "))
team1 = 0
team2 = 0
team3 = 0
team4 = 0

while votes > 0:
    user_vote = input(VOTE_MENU)

    if user_vote == "A":
        team1 += 1
    elif user_vote == "B":
        team2 += 1
    elif user_vote == "C":
        team3 += 1
    elif user_vote == "D":
        team4 += 1
    # Why do we use elif instead of just if-statements?

if team1 > team2 and team1 > team3 and team1 > team4:
    print("Team 1 has won!")
if team2 > team1 and team2 > team3 and team2 > team4:
    print("Team 2 has won!")
if team3 > team1 and team3 > team2 and team3 > team4:
    print("Team 3 has won!")
if team4 > team1 and team4 > team2 and team4 > team3:
    print("Team 4 has won!")
# Is there a better way we can store the votes for our teams?


# Password Checker
# one uppercase letter, one lowercase letter, and one digit
upper = False
lower = False
digit = False

while True:
    user_password = input("Please enter a password: ")

    for char in user_password:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper = True
        if char in "abcdefghijklmnopqrstuvwxyz":
            lower = True
        if char.isnumeric():
            digit = True

    message = ""
    if upper and lower and digit:
        message += "Thank you for entering a password!"
        break
    if not upper:
        message += "Missing uppercase character\n"
    if not lower:
        message += "Missing lowercase character\n"
    if not digit:
        message += "Missing digit"

print(message)


