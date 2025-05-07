n, m = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))
bag = [-1] * (m + 1)
bag[0] = 0
last_ind = 0
for i in range(n):
    start_ind = min(last_ind, m - weights[i])
    last_ind = start_ind + weights[i]
    for ind in range(start_ind, -1, -1):
        if bag[ind] != -1:
            target_ind = ind + weights[i]
            current_cost = bag[ind] + costs[i]
            if bag[target_ind] < current_cost:
                bag[target_ind] = current_cost
res = bag[-1]
for i in range(m, -1, -1):
    if bag[i] > res:
        res = bag[i]

print(res)
