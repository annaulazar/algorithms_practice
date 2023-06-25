# Богдан учится в Хогвартсе на факультете зельеварения. Завтра ему сдавать свой выпускной проект, но он ничего не успел
# подготовить. У него есть n ингредиентов, из которых можно сварить зелья. Зелье может состоять либо из одного
# ингредиента, либо из двух различных. Каждое зелье характеризуется его полезностью. Полезность — это целое
# число от -106 до 106. Богдану нужно сварить k зелий так, чтобы их суммарная полезность была максимальной
# (полезность зелья — это сумма полезностей ингредиентов, из которых оно состоит).
# Очень важно, чтобы все зелья в проекте были различны. Два зелья считаются различными, если найдется
# хотя бы один ингредиент, который отсутствует в одном зелье, но присутствует в другом.
# Помогите Богдану с проектом и подсчитайте максимальную суммарную полезность зелий, которую он может получить.

INF = int(1e18)
MAX_ELEM = int(1e9)


def check(minUS):
    ans = 0
    cnt = 0
    for i in range(1, n + 1):
        if usefulness[i] < minUS:
            break
        cnt += 1
        ans += usefulness[i]
    j = 2
    while j <= n and usefulness[1] + usefulness[j] >= minUS:
        j += 1
    for i in range(1, n + 1):
        if i + 1 >= j:
            break
        while j - 1 > i and usefulness[i] + usefulness[j-1] < minUS:
            j -= 1
        cnt += j - i - 1
        ans += prefsum[j-1] - prefsum[i] + usefulness[i] * (j - i - 1)
    if cnt >= k:
        return ans - (cnt - k) * minUS
    return INF


n, k = (int(x) for x in input().split())
usefulness = [int(i) for i in input().split()]
usefulness.sort()
usefulness.append(0)
usefulness.reverse()
prefsum = [0] * (n + 1)
for i in range(1, n + 1):
    prefsum[i] = prefsum[i - 1] + usefulness[i]

l = -MAX_ELEM
r = MAX_ELEM
while r > l:
    m = (r + l + 1) // 2
    if check(m) != INF:
        l = m
    else:
        r = m -1

print(check(l))
