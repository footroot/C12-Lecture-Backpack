def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


numbers = [23, 56, 90, 0, 45]

print(find_maximum(numbers))
