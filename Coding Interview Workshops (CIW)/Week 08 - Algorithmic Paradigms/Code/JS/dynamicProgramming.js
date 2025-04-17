/**
 * Dynamic Programming: Knapsack Problem 
 * Given items with weights and values, find the max value that can be carried.
 */

function knapsack(weights, values, capacity) {
    let n = values.length;
    // Create a matrix that is (capacity + 1 by n + 1)
    let dp = Array.from({ length: n + 1 }, () => Array(capacity + 1).fill(0));

    // For each item, pick an item if it doesn't exceed the capacity
    for (let i = 1; i <= n; i++) {
        for (let w = 0; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = Math.max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    return dp[n][capacity];
}

// Example Usage
console.log(knapsack([1, 2, 3], [10, 20, 30], 5));