# Дан массив из N целых чисел. Все числа от −109 до 109. Нужно уметь отвечать на запросы вида
# “Cколько чисел имеют значения от L до R?”.
# Формат ввода
# Число N (1≤N≤105). Далее N целых чисел. Затем число запросов K (1≤K≤105).
# Далее K пар чисел L,R (−109≤L≤R≤109) — собственно запросы.
# Формат вывода
# Выведите
# K чисел — ответы на запросы.

def lbinpoisk(l, r, num):
    while l < r:
        m = (l + r) // 2
        if nums[m] >= num:
            r = m
        else:
            l = m + 1
    return l


def rbinpoisk(l, r, num):
    while l < r:
        m = (l + r + 1) // 2
        if nums[m] <= num:
            l = m
        else:
            r = m - 1
    return r


n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
k = int(input())
ans = []
for _ in range(k):
    L, R = [int(x) for x in input().split()]
    if L > nums[-1] or R < nums[0]:
        res = 0
    else:
        res = rbinpoisk(0, n-1, R) - lbinpoisk(0, n-1, L) + 1
    ans.append(res)
print(*ans)
