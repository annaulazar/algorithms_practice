s = input()
n = len(s)
dp = [[1000, 1000] for _ in range(n + 1)]
dp[0][0] = 0
dp[0][1] = 1
for i in range(n):
    ll = 1 if (s[i] == 'L' or s[i] == 'B') else 0
    rr = 1 if (s[i] == 'R' or s[i] == 'B') else 0
    lr = ll + 1
    rl = rr + 1
    dp[i + 1][0] = min(dp[i][0] + ll, dp[i][1] + rl)
    dp[i + 1][1] = min(dp[i][1] + rr, dp[i][0] + lr)

print(dp[n][1])
