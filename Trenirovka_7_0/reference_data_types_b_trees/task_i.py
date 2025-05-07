n = int(input())
# родитель, масса, последний шар
snows = [(0, 0, 0)] * (n + 1)
res = 0
for i in range(1, n + 1):
    t, m = map(int, input().split())
    if m == 0:
        parent = snows[t][0]
        snows[i] = snows[parent]
    else:
        snows[i] = (t, snows[t][1] + m, m)
    res += snows[i][1]
print(res)
