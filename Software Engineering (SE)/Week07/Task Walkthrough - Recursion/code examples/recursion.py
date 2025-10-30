"""
Week 7
Recursion task walkthrough.
Code examples.
"""


def count_evens(num_list: list) -> int:
	"""
	Calculates the total of all even numbers in
	a list of numbers.

	:param num_list: list of numbers.
	:return: total sum of all even numbers.
	"""
	# Base case.
	if not num_list:
		return 0
	# Recursive case.
	else:
		print("Next arg:", num_list[1:])  # Trace table.
		if num_list[0] % 2 == 0:
			print("Return:", num_list[0])  # Trace table.
			return num_list[0] + count_evens(num_list[1:])
		else:
			return count_evens(num_list[1:])


print("=" * 15)
print("Example 1\n" + "=" * 15)
print("Stack Trace:")
number_list = [2, 1, 4, 5, 8]
print("\nResult using recursion:", count_evens(number_list))
# Example of solving the problem using
# standard iteration.
total_even = 0
for number in number_list:
	if number % 2 == 0:
		total_even += number
print("result using standard iteration:", total_even)


def reverse_list(input_list: list) -> list:
	"""
	Reverses the order of a given list.

	:param input_list: input list.
	:return: list reversed.
	"""
	# Base case:
	if not input_list:
		return []
	# Recursive case:
	my_return = input_list[-1]
	print("Return:", my_return)  # Trace table.
	print("Next arg:", input_list[:-1])  # Trace table.
	return [my_return] + reverse_list(input_list[:-1])


print("\n" + "=" * 15)
print("Example 2\n" + "=" * 15)
print("Stack Trace:")
original_list = [5, 6, 7, 8]
string_list = ["a", "b", "c", "d"]
print("\nResults using recursion:", reverse_list(original_list))
# Example of solving the problem using
# standard iteration.
result = []
for number in original_list:
	result.append(original_list[-1])
	original_list = original_list[:-1]
print("Result using standard iteration:", result)
