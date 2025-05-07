n = int(input())
a = list(map(int, input().split()))
q = int(input())
res = []
for _ in range(q):
    t, l, r, k = map(int, input().split())
    if t == 0:
        for i in range(l - 1, r):
            a[i] = k
    else:
        if a[l - 1: l + k - 1] == a[r - 1: r + k - 1]:
            res.append('+')
        else:
            res.append('-')
row = ''.join(res)
print(row)
