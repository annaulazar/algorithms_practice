import time
from random import randint


def rovers(n, s, volumes, costs, presses):
    dp = [{} for _ in range(n + 1)]
    dp[0] = {0: (0, 0, 1000000001)}

    for i in range(1, n + 1):
        for key in dp[i - 1]:
            if key not in dp[i]:
                dp[i][key] = dp[i - 1][key]
            new_cost = dp[i - 1][key][0] + costs[i - 1]
            new_volume = key + volumes[i - 1]
            new_presse = min(dp[i - 1][key][2], presses[i - 1])
            if new_volume <= s + new_presse:
                old_cost = dp[i - 1].get(new_volume, (0, 0))[0]
                if new_cost > old_cost:
                    dp[i][new_volume] = (new_cost, i, new_presse)

    max_cost = 0
    last_item = 0
    volume = 0
    res = []
    for key in dp[-1]:
        if dp[-1][key][0] > max_cost:
            max_cost = dp[-1][key][0]
            last_item = dp[-1][key][1]
            volume = key
    if last_item > 0:
        res.append(last_item)
    while last_item > 0:
        volume -= volumes[last_item - 1]
        last_item = dp[last_item - 1][volume][1]
        if last_item > 0:
            res.append(last_item)

    return(len(res), max_cost, reversed(res))

start_time = time.time()
n = 100
s = 1000000000
volumes = []
costs = []
presses = []
for _ in range(n):
    x = randint(500, 1000)
    y = randint(500000, 1000000)
    z = randint(500000000, 1000000000)
    volumes.append(x)
    costs.append(y)
    presses.append(z)
rovers(n, s, volumes, costs, presses)
print(time.time() - start_time)
