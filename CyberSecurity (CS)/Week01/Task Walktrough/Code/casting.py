"""
Create a program that declares the followin variables
name = "David"
weight = 88.4
birth_year = "1997"

create a variable called id_card and add the following data.
Add the user's: 
- name
- weight as a whole number
- age
- birth year. 

Display the information of the user by printing to the terminal.
"""

name = "David"
weight = 88.4
birth_year = "1997"
age = 2024 - int(birth_year)

weight = int(weight)

id_card = "Name: " + name + "\n"
id_card = id_card + "Birth year: " + birth_year + "\n"
id_card = id_card + "Age: " + str(age) + "\n"
id_card = id_card + "Weight: " + str(weight) + "\n"

print(id_card)