

num = input("Please enter a positive number: ")
num = int(num)
if num > 0:
    print(num)

while num > 0:
    print(num)
    num -= 1

secret_word = ""
while secret_word != "banana":
    secret_word = input("Guess the secret word: ")

# For loops
for i in range(1, 10):
    print(i)

for letter in "Hello":
    print(letter)

num = input("Please enter a number to see the multiplication table: ")
num = int(num)
print(f"Multiplication Table for {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# Break
while True:
    num = input("Please enter a number between 1 and 10: ")
    num = int(num)
    if 1 < num < 10:
        break


for i in range(1, 10):
    if i == 5:
        break

word = "bacon"
for letter in word:
    if letter == "o":
        print("Letter found!")
        break

# Continue
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)


word = "potatoes"
for letter in word:
    if letter in "aeiou":
        continue
    print(letter, end="")

# Use a for loop to reverse a string