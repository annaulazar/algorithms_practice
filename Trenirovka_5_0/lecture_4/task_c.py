def lbinpoisk(l, r, cnt, num):
    while l < r:
        m = (l + r) // 2
        if pref_a[m + cnt - 1] - pref_a[m - 1] >= num:
            r = m
        else:
            l = m + 1
    return l


n, m = map(int, input().split())
a = [int(x) for x in input().split()]
pref_a = [0] * (n + 1)
for i in range(1, n + 1):
    pref_a[i] = pref_a[i - 1] + a[i - 1]
for _ in range(m):
    k, s = map(int, input().split())
    index = lbinpoisk(1, n - k + 1, k, s)
    res = pref_a[index + k - 1] - pref_a[index - 1]
    if res == s:
        print(index)
    else:
        print(-1)
