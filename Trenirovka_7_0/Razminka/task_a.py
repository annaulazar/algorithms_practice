n = int(input())
dp = [0] * 36
dp[1] = 2
dp[2] = 4
dp[3] = 7
if n <= 3:
    print(dp[n])
else:
    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    print(dp[n])
