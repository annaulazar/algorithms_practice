n = int(input())
gv = [int(x) for x in input().split()]
gv.sort()
dp = [0] * (n + 1)
dp[1] = dp[2] = gv[1] - gv[0]
for i in range(3, n + 1):
    dp[i] = min(dp[i - 2], dp[i - 1]) + gv[i - 1] - gv[i - 2]
print(dp[n])
