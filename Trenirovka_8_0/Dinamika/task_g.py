n = int(input())

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j - 1]

print(dp[n][n])
