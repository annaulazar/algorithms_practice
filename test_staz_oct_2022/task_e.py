n, m, r = map(int, input().split())
orders = []
for _ in range(n):
    orders.append(list(map(int, input().split())))
maxsum = 0
for i in range(n):
    for j in range(m):
        if -r <= i + j <= r and -r <= i - j <= r:
            maxsum += orders[i][j]
sumrow = maxsum
print(maxsum)
for p in range(n):
    surrsum = sumrow
    for q in range(1, m):
        summinus = 0
        sumplus = 0
        for i in range(max(p - r, 0), p + 1):
            jmin = p + q - 1 - r - i
            jplus = i - p + q + r
            if 0 <= jmin <= m - 1:
                summinus += orders[i][jmin]
            if 0 <= jplus <= m - 1:
                sumplus += orders[i][jplus]
        for i in range(min(p + 1, n - 1), min(p + r, n - 1)):
            jmin = i - p + q - 1 - r
            jplus = p + q + r - i
            if 0 <= jmin <= m - 1:
                summinus += orders[i][jmin]
            if 0 <= jplus <= m - 1:
                sumplus += orders[i][jplus]
        surrsum -= summinus
        surrsum += sumplus
        maxsum = max(maxsum, surrsum)
    summinus = 0
    sumplus = 0
    for i in range(max(p - r, 0), p + 1):
        jmin = p + q - r - i
        if 0 <= jmin <= m - 1:
            summinus += orders[i][jmin]
        jmin = i - p + q + r
        if 0 <= jmin <= m - 1:
            summinus += orders[i][jmin]
    for i in range(min(p + 1, n - 1), min(p + 1 + r, n - 1)):
        jplus = i - p + q - 1 - r
        if 0 <= jplus <= m - 1:
            sumplus += orders[i][jplus]
        jplus = p + 1 + q + r - i
        if 0 <= jplus <= m - 1:
            sumplus += orders[i][jplus]
    sumrow -= summinus
    sumrow += sumplus
    maxsum = max(maxsum, sumrow)

print(maxsum)





# print(orders)
