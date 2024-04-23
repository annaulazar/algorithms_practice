n = int(input())
res = 0
for _ in range(n):
    a = int(input())
    res += a // 4
    a %= 4
    if a < 3:
        res += a
    else:
        res += 2
print(res)
