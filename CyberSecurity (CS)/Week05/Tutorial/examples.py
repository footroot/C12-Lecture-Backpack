def calculate_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

def calculate_median(numbers):
    numbers.sort()
    mid_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
        median = numbers[mid_index]
    else:
        median = (numbers[mid_index] + numbers[mid_index + 1]) / 2
    return median

# Main function
def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split(",")]
    
    average = calculate_average(numbers)
    print(f"The average is: {average}")
    
    median = calculate_median(numbers)
    print(f"The median is: {median}")

main()
