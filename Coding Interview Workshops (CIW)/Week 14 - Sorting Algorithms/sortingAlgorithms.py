# Bubble Sort: Swap adjacent elements if they are in the wrong order
# Simple to implement, but inefficient
# (Avg and worse) Time complexity -> O(n^2)
# (Best) time complexity -> O(n)
# Use case: small datasets, nearly sorted lists

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Selection Sort: Like Bubble Sort -> Find the smallest, put that in the front
# Not stable
# Time complexity -> O(n^2)
# Doesn't improve time complexity if list is nearly sorted

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Merge Sort: Divide-and-conquer sorting algorithm
# Stable
# Time complexity: O(n log n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i, j, k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        arr[k:] = L[i:] + R[j:]

# Quick Sort -> Like merge sort but with no optimization
# Filter left and right sublists to include only elements less than or more than
# Not stable
# Time complexity: O(n^2)

# Heap Sort -> Making use of a Heap data structure
# Not stable
# Time complexity: O(n log n)


# Counting Sort: Build our array in order by counting how many of each element we have
# Only works for integer array
# O(n+k) -> k number of unique values
# Ideal if range is very small

def count_sort(arr):
    count = [0] * max(arr) + 1
    for num in arr:
        count[num] += 1
    index = 0
    for i, c in enumerate(count):
        arr[index:index+c] = [i]*c
        index += c

# Radix Sort: Process digits from least to most significant