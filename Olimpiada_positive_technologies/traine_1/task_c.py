def rbinpoisk(l, r, num):
    while l < r:
        m = (l + r + 1) // 2
        if s[m] >= num:
            l = m
        else:
            r = m - 1
    return r


n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)

res = 0
for index, elem in enumerate(s):
    target = 0.9 * elem
    index1 = rbinpoisk(index + 1, n - 1, target)
    if s[index1] >= s[index] * 0.9:
        res += index1 - index

print(res)
