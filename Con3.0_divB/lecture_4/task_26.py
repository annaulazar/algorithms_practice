n, m = map(int, input().split())
table = [[0] * (m + 1) for _ in range(n + 1)]
for j in range(2, m + 1):
    table[0][j] = 20000
for i in range(2, n + 1):
    table[i][0] = 20000
for i in range(1, n + 1):
    row = [int(x) for x in input().split()]
    for j in range(1, m + 1):
        table[i][j] = min(table[i][j - 1], table[i - 1][j]) + row[j - 1]
print(table[-1][-1])
