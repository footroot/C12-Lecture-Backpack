// Let's solve a problem together using the method we just learnt!
// Our problem is:
// Given an array of integers, find two numbers that add up to a target sum.

// 1. Understand the problem
// - Inputs: Array (lists) -> how are we getting them?, Integers -> how strict?, Integer (sum), Negative Ints
// - Outputs: 2 integer -> how do we return this?
// - [1, 2, 3, 4, 7], 7 -> [3, 4]

// - Edge Cases: our list is empty -> return [], 
// if the answer doesn't exist -> return [], 
// multiple solutions -> return the first one we find, 
// duplicate values -> we won't have duplicates, 
// only one value in our list -> return [], 
// target sum is in the list -> we can't use it unless zero is in the list as well
// - Constraints: same integer twice -> we can't do that, only use 2 numbers, you can add them, they only be in the list

// 2. Plan the solution
// - Brute force: Loop through the list, for each element loop through the rest of the list checking each sum whether it equals target O(n2)
// - Optimised solution: HashTable (dictionary, map) -> for loop check if complement in hashtable each element store complement as key, element as the value O(n)

// 3. Code, then go back and optimise
function twoSum (intList, targetSum){
    if (intList.length < 2)
        return [];

    for (let i = 0; i < intList.length; i++){
        let a = intList[i]
        for (let j = i+1; j < intList.length; j++){
            if ((a + intList[j]) == targetSum)
                return [a, intList[j]];
        }
            
    }
        
    return [];
}
    

console.log(twoSum([1, 2, 3, 4, 7], 7));

// 4. Iterate based on feedback and optimise!
function twoSumOpt (intList, targetSum){
    if (intList.length < 2)
        return [];

    let comp = new Map();
    for (let i = 0; i < intList.length; i++){
        let a = intList[i];
        if (comp.has(a))
            return [a, comp.get(a)];
        
        comp.set(targetSum-a, a);
    }

    return [];
}

console.log(twoSumOpt([1, 2, 3, 4, 7], 7))