def solve_knapsack(capacity, weight, values):
    if capacity <= 0 or not values:
        return 0, [[0]]
    
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dont_take = dp[i-1][w]
            
            if weight[i-1] <= w:
                take = values[i-1] + dp[i-1][w - weight[i-1]]
                dp[i][w] = max(dont_take, take)
            else:
                dp[i][w] = dont_take
    
    return dp[n][capacity], dp