MOD = 10**9 + 7

# Read the input values n and m
n, m = map(int, input().split())

# Initialize a DP array to store the number of ways
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Base cases
dp[0][0] = 1

# Calculate the number of ways for each cell in the grid
for i in range(n + 1):
    for j in range(m + 1):
        if i + 1 <= n:
            dp[i + 1][j] += dp[i][j] * (j % 2 == 0)
            dp[i + 1][j] %= MOD
        if j + 1 <= m:
            dp[i][j + 1] += dp[i][j] * (i % 2 == 0)
            dp[i][j + 1] %= MOD

# Print the number of ways modulo 10^9+7
print(dp[n][m])
