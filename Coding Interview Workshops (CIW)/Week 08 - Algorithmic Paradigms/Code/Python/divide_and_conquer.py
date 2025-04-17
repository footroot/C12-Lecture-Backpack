"""
Divide and Conquer: QuickSort
Uses recursion to partition elements and sort them efficiently.

"""

def quicksort(arr):
    # Return element if length of array is 1
    if len(arr) <= 1:
        return arr
    
    # Find the middle most element, create an array of 
    # all elements less than pivot and more than pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Sort left and right array and combine results
    return quicksort(left) + middle + quicksort(right)