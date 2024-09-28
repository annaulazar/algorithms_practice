import math


def check_ost(y_):
    ost = s
    for _ in range(n):
        ost -= y_
        ost = math.ceil(ost * (1 + p / 100))
    return ost <= 0


def lbinpoisk(l, r):
    while l < r:
        m = (l + r) // 2
        if check_ost(m):
            r = m
        else:
            l = m + 1
    return l


s, n, p = map(int, input().split())
y = lbinpoisk(1, s)

print(y)
