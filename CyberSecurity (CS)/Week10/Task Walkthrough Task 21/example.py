# user_input = input("Please enter an equation to evaluate: ")
# print(eval(user_input))
# __import__('os').system('dir')


import os

if os.path.exists('input.txt'):
    with open('input.txt', "r", encoding='utf-8') as file:
        number = file.read().strip()
else:
    number = input("Please enter a number: ")

if number.isnumeric():
    number = int(number)
    print({number} * 2)
else:
    print("Invalid values.")
