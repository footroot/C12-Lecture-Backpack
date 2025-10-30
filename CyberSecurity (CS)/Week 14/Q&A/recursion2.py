def reverse_str(curr_str):
    new_str = ""
    for letter in curr_str:
        new_str = letter + new_str
    return new_str

def reverse_str_r(curr_str):
    if len(curr_str) == 1:
        return curr_str
    return reverse_str_r(curr_str[1:]) + curr_str[0]
 #                     "olleH"

print(reverse_str_r("Hello"))