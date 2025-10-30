def walk_recursive(steps):
    if steps == 0:
        return 1
    walk_recursive(steps - 1)
    print(steps)

walk_recursive(10)

def walk(steps):
    if steps > 0:
        for i in range(steps):
            print(i)



def add_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return num


def add_numbers(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + add_numbers(numbers[1:])
#             1     + add_numbers([2,3,4])           
#                              2          +  add_numbers([3,4])
#                                                   3      +     add_numbers([4])
#                                                                        4

print(add_numbers([1,2,3,4]))