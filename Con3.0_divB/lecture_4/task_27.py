n, m = map(int, input().split())
table = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = [int(x) for x in input().split()]
    for j in range(1, m + 1):
        table[i][j] = max(table[i][j - 1], table[i - 1][j]) + row[j - 1]
print(table[-1][-1])
res = []
while m > 1 or n > 1:
    temp_d = {table[n][m - 1]: ('R', 0, -1), table[n - 1][m]: ('D', -1, 0)}
    temp = temp_d[max(temp_d)]
    res.append(temp[0])
    n += temp[1]
    m += temp[2]
print(*res[::-1])
