n, m = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))
dp = [[(-1, -1)] * (m + 1) for _ in range(n + 1)]
dp[0][0] = (0, 0)
max_ind = 0
for i in range(1, n + 1):
    max_ind = min((max_ind + weights[i - 1]), m)
    for j in range(0, max_ind + 1):
        dp[i][j] = dp[i - 1][j]
        if weights[i - 1] <= j and dp[i - 1][j - weights[i - 1]][0] != -1:
            new_cost = dp[i - 1][j - weights[i - 1]][0] + costs[i - 1]
            if new_cost > dp[i][j][0]:
                dp[i][j] = (new_cost, i)

max_cost = 0
last_item = 0
weight = 0
res = []
for j in range(1, m + 1):
    if dp[-1][j][0] > max_cost:
        max_cost = dp[-1][j][0]
        last_item = dp[-1][j][1]
        weight = j
if last_item != 0:
    res.append(last_item)
while last_item > 0:
    weight -= weights[last_item - 1]
    last_item = dp[last_item - 1][weight][1]
    if last_item > 0:
        res.append(last_item)

print(*reversed(res), sep='\n')
