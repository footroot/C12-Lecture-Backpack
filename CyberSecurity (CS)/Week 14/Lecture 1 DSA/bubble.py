def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if any swaps occur
        for j in range(n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if out of order
                swapped = True
        if not swapped:  # If no swaps occurred, array is already sorted
            break
    return arr


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = bubble_sort(arr)
print(sorted_arr)

