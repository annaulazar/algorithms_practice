# Дана последовательность чисел и запросы вида "определите сколько положительных чисел"
# "на отрезке с индексами от L до R".

n = int(input())
in_list = [int(x) for x in input().split()]
pref_positiv = [0] * (n + 1)
for i in range(1, n + 1):
    if in_list[i - 1] > 0:
        pref_positiv[i] = pref_positiv[i - 1] + 1
    else:
        pref_positiv[i] = pref_positiv[i - 1]

k = int(input())
for i in range(k):
    a, b = (int(x) for x in input().split())
    print(pref_positiv[b] - pref_positiv[a - 1])

