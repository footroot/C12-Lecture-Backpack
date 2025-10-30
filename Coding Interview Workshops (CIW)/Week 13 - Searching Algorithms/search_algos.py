# Linear search: unsorted array
def linear_search(arr, target):
    for i, n in enumerate(arr):
        if n == target:
            return i
    return -1

# Binary search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while (low <= high):
        mid = (high - low) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else: 
            high = mid - 1
    return -1

size = int(input("How big is the list?"))
array = range(0, size)
print(linear_search(array, size))

# Ternary search
def ternary_search(arr, target):
    low = 0
    high = len(arr)-1

    while (low <= high):
        mid1 = (high - low) // 3
        mid2 = 2*(mid1)

        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif target > arr[mid1]:
            if target > arr[mid2]:
                low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1
        else: 
            high = mid1 - 1
    return -1

# Exponential search
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    i = 1
    while (i < len(arr)) and (arr[i] <= target):
        i *= 2
    
    return binary_search(arr[:min(i, len(arr))], target)



# Upper/Lower Bound: WORKS OPPOSITE -> low stores number greater than 
# or equal to target, high stores number less than or equal to target
def bound(arr, target):
    low = 0
    high = len(arr)-1

    while (low < high):
        mid = (high - low) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else: 
            high = mid - 1

    # For >=
    return low
    # For <=
    # return high

    


