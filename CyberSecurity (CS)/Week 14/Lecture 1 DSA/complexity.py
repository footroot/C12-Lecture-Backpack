# O(1)
def get_value(my_list, key):
    return my_list[key]

# print(get_value([1,2,3,4,5], 1))

def add_values(num1, num2):
    num1 += 1
    return num1 + num2


def get_values(my_list, keys):
    values = []
    for key in keys:                     
        values.append(my_list[key])
    return values

    # O(n)


def print_all(my_list):
    for item in my_list:
        pass

    for _ in range(len(my_list)): # n
        for item in my_list:      # n
            print(item)

print_all([1,2,3,4,5])
# O(n^2)