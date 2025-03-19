/**
 * 
 * Divide and Conquer: QuickSort
 * Uses recursion to partition elements and sort them efficiently.
 * 
 */

function quickSort(arr) {
    // Return element if length of array is 1
    if (arr.length <= 1) {
        return arr;
    }

    // Find the middle most element, create an array of 
    // all elements less than pivot and more than pivot
    let pivot = arr[Math.floor(arr.length / 2)];
    let left = arr.filter(x => x < pivot);
    let middle = arr.filter(x => x === pivot);
    let right = arr.filter(x => x > pivot);
    
    // Sort left and right array
    return [...quickSort(left), ...middle, ...quickSort(right)];
}