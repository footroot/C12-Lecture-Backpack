my_list = ["James", "Amy", "Peter", "Michelle"]

my_list.append("David")

my_list.extend(["Tina", "Parker"])

my_list += ["Victoria", "Adam"]

my_list.reverse()

my_list.remove("Adam")
my_list.pop(3)
del my_list[0]

# my_list.clear()
# print(my_list)


# for i, name in enumerate(my_list, 1):
#     print(f"{i}: {name}")

# for i in range(len(my_list)):
#     print(f"Index {i}: {my_list[i]}")

num_list = [1,2,3,4,5,6]
squared_list = [x**2 for x in num_list]
# for num in num_list:
#     squared_list.append(num**2)
# print(squared_list)

# my_list = ["James", "Amy", "Peter", "Michelle"]
# initials = [name[0] for name in my_list]
# print(initials)

# empty_list = ["" for i in range(10)]
# print(empty_list)

# for i in range(10):
#     user_input = input("Please enter something: ")
#     # Check for valid input
#     my_list.append(user_input)

computer = {
    "processor" : "Ryzen 7 7700x",
    "ram" : "16GB DDR5",
    "storage" : "512GB SSD"
}

# print(computer["processor"])
# print(computer.get("ram"))

# computer['storage'] = "1TB SSD"
# computer.update(graphics_card="NVIDIA GeForce RTX 3060")

# for key in computer:
#     print(key)

# for value in computer.values():
#     print(value)

# for key, value in computer.items():
    # print(key, value, sep=" - ")

numbers = [1,2,3,4,5,6]

numbers2 = numbers.copy()

numbers2[2] = 99

# print(numbers)
# print(numbers2)

data = {'name': "jake", "age": 34}

data2 = data.copy()
data2['name'] = "Brenda"

# print(data)

# Deepcopy
my_numbers = [[1,2,3],[4,5,6]]

def add_values(values):
    total = 0
    for value in values:
        total += value
    return total

my_values = [1,2,3,4,5]
print(add_values(my_values))

def add_one(num_list):
    for i in range(len(num_list)):
        num_list[i] += 1

my_list = [1,2,3,4,5]
add_one(my_list)
print(my_list)