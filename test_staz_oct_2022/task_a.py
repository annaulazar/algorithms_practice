from random import randint

def maxprefsuf(lst1, lst2):
    res = 0
    suf = 0
    pref = 0
    while pref < len(lst1) and suf < len(lst2):
        while suf < len(lst2) - 1 and lst1[pref] != lst2[suf]:
            suf += 1
        if lst1[pref] == lst2[suf]:
            res += 1
        if suf >= len(lst2) - 1 or pref >= len(lst1) - 1:
            break
        suf += 1
        if lst2[suf] == lst1[pref + 1]:
            pref += 1
        else:
            res = 0
    return res

kmas = []
for _ in range(3):
    n, *k = map(int, input().split())
    kmas.append(k)
prefsuf = {}
for i, lst1 in enumerate(kmas):
    for j, lst2 in enumerate(kmas):
        if i != j:
            prefsuf[(i, j)] = maxprefsuf(lst1, lst2)
firstpar = max(prefsuf.values())
for key, value in prefsuf.items():
    if value == firstpar:
        break
first = kmas[key[1]] + kmas[key[0]][value:]
secondind = list({0, 1, 2} - set(key))[0]
second = kmas[secondind]
prefsum1 = maxprefsuf(first, second)
prefsum2 = maxprefsuf(second, first)
if prefsum1 >= prefsum2:
    res = second + first[prefsum1:]
else:
    res = first + second[prefsum2:]
print(len(res))
print(*res)


# def main():
#     prefsuf = {}
#     for i, lst1 in enumerate(kmas):
#         for j, lst2 in enumerate(kmas):
#             if i != j:
#                 prefsuf[(i, j)] = maxprefsuf(lst1, lst2)
#     firstpar = max(prefsuf.values())
#     for key, value in prefsuf.items():
#         if value == firstpar:
#             break
#     first = kmas[key[1]] + kmas[key[0]][value:]
#     secondind = list({0, 1, 2} - set(key))[0]
#     second = kmas[secondind]
#     prefsum1 = maxprefsuf(first, second)
#     prefsum2 = maxprefsuf(second, first)
#     if prefsum1 >= prefsum2:
#         res = second + first[prefsum1:]
#     else:
#         res = first + second[prefsum2:]
#     return res
#
# kmas = []
# for _ in range(3):
#     k = [randint(1, 10) for _ in range(randint(1, 5))]
#     kmas.append(k)
# print(*kmas, sep='\n')
# res = main()
# print(len(res))
# print(*res)
