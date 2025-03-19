'''
Dynamic Programming: Knapsack Problem
Given items with weights and values, find the max value that can be carried.

'''

def knapsack(weights, values, capacity):
    n = len(values)

    # Create a matrix that is (capacity + 1 by n + 1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # For each item, pick an item if it doesn't exceed the capacity
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]