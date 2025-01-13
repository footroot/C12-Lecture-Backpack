# Numerical Analysis
# Three scores 
reading = float(input("Enter a reading time: "))
planning = float(input("Enter a planning time: "))
typing = float(input("Enter a typing time: "))


# Sum, average, product
sum = reading+planning+typing
average = sum / 3
product = reading*planning*typing

# Highest, lowest
max([reading, typing, planning])
min

# Compare to a benchmark (7)
if (reading > 7):
    print("Well done!")

list = []
# input 
list.append(1)
list.append(0)
list.append(67)
list.append(8)

i = 0
sum = 0
average = 0

while (i < len(list)):

    if (list[i] == 0):
        print("Invalid input!")
        break

    sum = sum + list[i]
    average = list[i]/len(list)
    i = i+1

average = sum/len(list)