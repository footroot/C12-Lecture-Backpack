my_bool = True

# print(type(my_bool))

is_raining = False
logged_in = True

is_smaller = (15 <= 15)
is_larger = (20 >= 7)
is_equal = ("Hello" == "hello")

# print(is_smaller)
# print(is_larger)
# print(is_equal)


if False:
    print("If this prints the condition is True!")


is_raining = False
if is_raining:
    print("It is raining outside!")


rain_volume = 1
if rain_volume > 2:
    is_raining = True

# if is_raining:
#     print("It is raining outside!")
# else:
#     print("It is not raining outside!")


num1 = 5
num2 = 10

if num1 == num2:
    print("The number are equal!")
elif num1 > num2:
    print(f"{num1} is larger than {num2}!")
else:
    print(f"{num2} is larger than {num1}!")


# Create a program that will ask a user to provide their
# Last 3 test scores and determine their grade average.
# 90-100 - A
# 80-89  - B
# 70-79  - C
# 60-69  - D
# 50-59  - E
# < 50   - F

score1 = input("Please enter the 1st score: ")
score2 = input("Please enter the 2nd score: ")
score3 = input("Please enter the 3rd score: ")

score1 = int(score1)
score2 = int(score2)
score3 = int(score3)

total = score1 + score2 + score3
average = total/3

if average >= 90:
    print("Grade Score: A")
elif average >= 80:
    print("Grade Score: B")
elif average >= 70:
    print("Grade Score: C")
elif average >= 60:
    print("Grade Score: D")
elif average >= 50:
    print("Grade Score: E")
else:
    print("Failed")
