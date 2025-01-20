def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # divide list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # recursively sort the two halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    # implement the merge function
    pass
