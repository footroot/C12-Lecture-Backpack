my_list = [1,2,3,4,5]

new_list = my_list

new_list[0] = 300

# print(my_list)
# print(new_list)


list_2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(list_2d[1][1])
# print(list_2d[2][2])
from copy import deepcopy

new_list_2d = deepcopy(list_2d)

new_list_2d[1][1] = "x"

print(list_2d)
print(new_list_2d)