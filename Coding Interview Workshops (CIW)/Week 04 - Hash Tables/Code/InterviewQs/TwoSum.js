/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// APC
// Assumptions:
// Each input has one solution
// Can't use the same element twice
// Return answer in any order
// Efficient time wise solution
// nums is small
// int and target are big

// Plan:
// 1. Obvious solution: Look at each number, loop through rest try and form target [O(n2)]
// 2. Better solution: Searching more efficient with Hash Tables
// for each element: {key = value, index}, then check if the complement is in the map already
// is [2] in the list -> yes / no
// O(n)


var twoSum = function (nums, target) {
    let valueMap = new Map();

    for (let i = 0; i < nums.length; i++) {
        let comp = target - nums[i];
        if (valueMap.has(comp)) {
            return [i, valueMap.get(comp)];
        }
        valueMap.set(nums[i], i)
    }
};