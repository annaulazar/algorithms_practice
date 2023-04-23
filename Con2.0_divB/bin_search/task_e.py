# Даны n точек на прямой, нужно покрыть их k отрезками одинаковой длины ℓ.
# Найдите минимальное ℓ.
# Формат ввода
# На первой строке n (1≤n≤105) и k (1≤k≤n). На второй n чисел xi (∣xi∣≤109).
# Формат вывода
# Минимальное такое ℓ, что точки можно покрыть k отрезками длины ℓ.

def check(long):
    count = 1
    startpos = x[0]
    endpos = startpos + long
    for pos in x:
        if pos > endpos:
            startpos = pos
            endpos = startpos + long
            count += 1
    return count <= k


def lbinpoisk(l, r):
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1
    return l

n, k = [int(i) for i in input().split()]
x = [int(j) for j in input().split()]
x.sort()
L = 0
R = x[-1] - x[0]
print(lbinpoisk(L, R))
