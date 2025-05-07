n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
moods = list(map(int, input().split()))
interest = [(x[0], x[1], ind + 1) for ind, x in enumerate(zip(a, b))]
useful = interest.copy()
interest.sort(key=lambda y: (-y[0], -y[1], y[2]))
useful.sort(key=lambda y: (-y[1], -y[0], y[2]))
used = [0] * (n + 1)
cursor0 = 0
cursor1 = 0
answer = [0] * n
for i in range(n):
    if moods[i]:
        while cursor1 < n and used[useful[cursor1][2]]:
            cursor1 += 1
        if cursor1 < n:
            pos = useful[cursor1][2]
            answer[i] = pos
            used[pos] = 1
    else:
        while cursor0 < n and used[interest[cursor0][2]]:
            cursor0 += 1
        if cursor0 < n:
            pos = interest[cursor0][2]
            answer[i] = pos
            used[pos] = 1
print(*answer)
