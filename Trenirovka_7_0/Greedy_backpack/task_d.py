n, m = map(int, input().split())
ingots = list(map(int, input().split()))
bag = [False] * (m + 1)
bag[0] = True
last_ind = 0
for ingot in ingots:
    start_ind = min(last_ind, m - ingot)
    last_ind = start_ind + ingot
    for ind in range(start_ind, -1, -1):
        if bag[ind]:
            target_ind = ind + ingot
            bag[target_ind] = True
for i in range(m, -1, -1):
    if bag[i]:
        print(i)
        break