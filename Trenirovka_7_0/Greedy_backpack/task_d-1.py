# D. Рюкзак: наибольший вес
# Дано N золотых слитков массой m1, …, mN . Ими наполняют рюкзак, который выдерживает вес не более M.
# Какую наибольшую массу золота можно унести в таком рюкзаке?
# С восстановлением ответа


n, m = map(int, input().split())
ingots = [0] + list(map(int, input().split()))
bag = [-1] * (m + 1)
bag[0] = 0
last_ind = 0
for (i, ingot) in enumerate(ingots):
    start_ind = min(last_ind, m - ingot)
    last_ind = start_ind + ingot
    for ind in range(start_ind, -1, -1):
        if bag[ind] != -1:
            target_ind = ind + ingot
            if bag[target_ind] == -1:
                bag[target_ind] = i
res = []
answer = 0
for i in range(m, -1, -1):
    if bag[i] != -1:
        current = i
        answer = i
        while bag[current] != 0:
            res.append(bag[current])
            current = current - ingots[bag[current]]
        break

print(answer)
print(*sorted(res))