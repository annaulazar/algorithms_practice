n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = []
for i in range(n):
    temp = 0
    for j in range(n):
        if i != j:
            temp |= a[i][j]
    res.append(temp)
print(*res)