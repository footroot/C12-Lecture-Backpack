# O(1)
def greet(my_list):
    return my_list[-1]


# O(n)
def print_list(my_list):
    for item in my_list:
        print(item)


# O(n^2)
def print_double(my_list):
    for i in range(len(my_list)):
        for item in my_list:
            print(item, end=" ")
        print()

print_double([1,1,1,1])


