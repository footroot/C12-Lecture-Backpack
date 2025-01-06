print("Welcome to the CS bootcamp!")
print(100)

word = input("Please enter a random word: ")

# Data types
# Strings
my_str = "apples"
my_str2 = 'pears'

print(my_str.upper())
print(my_str.title())
print(my_str.replace("le", ""))
print(len(my_str))

# String formating
new_str = my_str + " and " + my_str2
new_str = f"{my_str} and {my_str2}"
new_str = "{} and {}".format(my_str, my_str2)
print(new_str)

# apples
# 012345
print(my_str[0:3]) # app
print(my_str[2:])  # ples

# pears
# 01234
# print 'ear'
print(my_str2[1:4])


# Numbers
num1 = 5
num2 = 8
num3 = 15.5

add1 = num1 + num2
add2 = num2 + num3
print(add1)
print(add2)

sub1 = num2 - num1
sub2 = num3 - num2
print(sub1)
print(sub2)

mul = num1 * num2
print(mul)

div = num2/num1
print(div)

my_bool = True
my_bool2 = False

# Casting
# Str Int interaction
result = "3" + 5 # cast "3" to int/ cast 5 to str
print(result)

result = "3" * 5
print(result)

str_to_int = int("34")
int_to_str = str(2024)
int_to_float = float(10)
str_to_float = float("12.2")

# Checking type
print(type(str_to_int))