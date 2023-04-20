n = int(input())
price = [int(input()) for _ in range(n)]
table = [[0] * (n + 2) for _ in range(n + 1)]
for j in range(1, n + 2):
    table[0][j] = 3000000
for i in range(1, n + 1):
    for j in range(0, n + 2):
        if j > i:
            table[i][j] = 3000000
        elif price[i - 1] > 100:
            table[i][j] = min((table[i - 1][j - 1] + price[i - 1]), table[i - 1][j + 1])
        else:
            table[i][j] = min((table[i - 1][j] + price[i - 1]), table[i - 1][j + 1])
ans = table[-1][0]
k1 = 0
for j in range(1, n + 1):
    if table[-1][j] <= ans:
        ans = table[-1][j]
        k1 = j
i, j = n, k1
k2 = 0
res = []
while i > 0:
    if price[i - 1] > 100:
        if table[i - 1][j - 1] + price[i - 1] > table[i - 1][j + 1]:
            k2 += 1
            res.append(i)
            j += 1
        else:
            j -= 1
    else:
        if table[i - 1][j] + price[i - 1] > table[i - 1][j + 1]:
            k2 += 1
            res.append(i)
            j += 1
    i -= 1
print(ans)
print(k1, k2)
print(*res[::-1])
