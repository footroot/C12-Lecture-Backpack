def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case

    pivot = arr[len(arr) // 2]  # Pivot element (middle element)

    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)
