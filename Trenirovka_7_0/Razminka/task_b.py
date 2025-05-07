n = int(input())
times = [[4000, 4000, 4000], [4000, 4000, 4000]]
for _ in range(n):
    times.append(list(map(int, input().split())))
dp = [0] * (n + 3)
for i in range(3, n + 3):
    dp[i] = min(dp[i - 1] + times[i - 1][0],
                dp[i - 2] + times[i - 2][1],
                dp[i - 3] + times[i - 3][2])
print(dp[n + 2])
