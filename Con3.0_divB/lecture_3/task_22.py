n, k = map(int, input().split())
dp = [0] * max((n + 1), (k + 2))
dp[1] = 1
for i in range(2, k + 2):
    dp[i] = 2 ** (i - 2)
for j in range(k + 2, n + 1):
    dp[j] = sum(dp[j - k: j + 1])
print(dp[n])
