n, k = map(int, input().split())
a = list(map(int, input().split()))

d = {}
for task in a:
    if task not in d:
        d[task] = 0
    d[task] += 1

themes = sorted([(value, key) for key, value in d.items()])
themes_n = len(themes)

ost = k % themes_n

res = []
for cnt, theme in themes:
    first = min(cnt, k // themes_n)
    second = min(cnt - first, ost)
    if k < themes_n:
        second = min(second, 1)
    ost -= second
    if first < k // themes_n:
        ost += k // themes_n - first
    res.extend([theme] * (first + second))

print(*res)
