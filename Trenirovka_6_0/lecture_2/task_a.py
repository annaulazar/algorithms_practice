n = int(input())
a = list(map(int, input().split()))
pref = [0] * n
pref[0] = a[0]
for i in range(1, n):
    pref[i] = pref[i - 1] + a[i]
print(*pref)
