def superEggDrop(K: int, N: int) -> int:
    # dp[k][n] = minimum number of attempts with k eggs and n floors
    # Base cases:
    # dp[1][n] = n (With 1 egg, we need n tries for n floors - worst case linear search)
    # dp[k][0] = 0 (With 0 floors, we need 0 tries)
    # dp[k][1] = 1 (With 1 floor, we need 1 try)

    dp = [[0] * (N + 1) for _ in range(K + 1)]

    for n in range(1, N + 1):
        dp[1][n] = n

    print(dp[0])
    print(dp[1])
    for k in range(2, K + 1):
        for n in range(1, N + 1):
            dp[k][n] = float('inf')
            # Compute dp[k][n] by testing from floor x = 1 to n
            for x in range(1, n + 1):
                # If egg breaks at floor x: dp[k-1][x-1]
                # If egg doesn't break: dp[k][n-x]
                # We take the worst of these two (since we need to guarantee worst-case)
                # plus one attempt for dropping at floor x.
                worst_case = 1 + max(dp[k - 1][x - 1], dp[k][n - x])
                dp[k][n] = min(dp[k][n], worst_case)

    return dp[K][N]


# Example usage:
k = 10
n = 100
print(superEggDrop(k, n))
