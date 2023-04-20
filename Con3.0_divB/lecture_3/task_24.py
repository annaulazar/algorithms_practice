n = int(input())
tickets = [[3601, 3601, 3601]]
for _ in range(n):
    tickets.append(list(map(int, input().split())))
for _ in range(2):
    tickets.append([3601, 3601, 3601])
dp = [0] * (n + 3)
for i in range(1, n + 1):
    dp[i] = min((dp[i - 1] + tickets[i][0]), (dp[i - 2] + tickets[i - 1][1]),
                (dp[i - 3] + tickets[i - 2][2]))
print(dp[n])
