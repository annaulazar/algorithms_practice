def lbinpoisk(l, r):
    while l < r:
        m = (l + r) // 2
        res = ((a + m - 1) // m) * ((b + m - 1) // m)
        if res <= k:
            r = m
        else:
            l = m + 1
    return l

a, b, k = map(int, input().split())
s = lbinpoisk(1, a * b)

print(s)
