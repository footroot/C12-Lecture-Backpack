
// Common String Manipulation Techniques:
// - Substrings: splicing, substring -> string[start=0:stop=-1:step=1], string.slice(start, stop, step)
// - Character access: indexing, charAt() -> string[indexOfChar], charAt(index)
// - Concatenation: combining strings -> +, +=, string.join(joinString)
// - Searching: find location of substring -> string.find("substring"), 
// substring in string, string.includes(substring), string.indexOf(substring)
// - Replacement and Case Conversion: string.replace(replace, with), replaceAll, 
// lower(), upper(), toLowerCase(), toUpperCase()
// - Reversing: .reverse(), [start=-1:stop=0:-1]

// Optimization Approaches:
// - Sliding Window Technique - Dynamic Programming (technically)
// Maintain a window [start ... end]
// Slide across the string

/**[1, 2, 3, 4, 5] -> k = 3
6
6 + 4 - 1 = 9
9 + 5 - 2 = 12

[happy birthdy] -> [birthday]
*/

function slidingWindow(arr, k) {
    let currentSum = arr.slice(0, k).reduce((a, b) => a + b, 0);
    let maxSum = currentSum;
    for (let i = k; i < arr.length; i++) {
        currentSum += arr[i] - arr[i - k];
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
}

let s = "anagram";
let count = {};
for (let char of s) {
    count[char] = (count[char] || 0) + 1;
}
console.log(count['a']);  // 3


// Time & Space Complexity of String Methods:


