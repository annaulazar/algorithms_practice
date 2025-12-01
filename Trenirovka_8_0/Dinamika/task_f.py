n = int(input())
table = []
for _ in range(n):
    table.append(list(input().strip()))

dp = [[-100000] * 5 for _ in range(n + 1)]
dp[0][1] = 0
dp[0][2] = 0
dp[0][3] = 0

costs = {'W': -100000, '.': 0, 'C': 1}
for i in range(1, n + 1):
    for j in range(1, 4):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + costs[table[i - 1][j - 1]]

res = max(sum(dp, []))
print(max(0, res))
