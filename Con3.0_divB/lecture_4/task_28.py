n, m = map(int, input().split())
table = [[0] * (m + 2) for _ in range(n + 2)]
table[1][1] = 1
for i in range(2, n + 1):
    for j in range(2, m + 1):
        table[i][j] = sum((table[i - 1][j - 2], table[i - 2][j - 1]))
print(table[n][m])

