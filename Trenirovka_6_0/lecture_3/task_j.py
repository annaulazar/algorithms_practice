from collections import deque


n, H = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))
chairs = list(zip(h, w))
chairs.sort()

dif = [0] * n
for i in range(1, n):
    dif[i] = chairs[i][0] - chairs[i - 1][0]

que = deque()
temp = chairs[0][1]
right = 0
que.append((dif[0], 0))
while temp < H and right < (n - 1):
    right += 1
    temp += chairs[right][1]
    while que and dif[right] > que[-1][0]:
        que.pop()
    que.append((dif[right], right))
min_dif = que[0][0]
for left in range(1, n):
    temp -= chairs[left - 1][1]
    if que[0][1] <= left:
        que.popleft()
    while temp < H and right < (n - 1):
        right += 1
        temp += chairs[right][1]
        if left == right:
            que = deque()
            que.append((0, left))
        else:
            while que and dif[right] > que[-1][0]:
                que.pop()
            que.append((dif[right], right))
    if left == right:
        que = deque()
        que.append((0, left))
    if temp >= H:
        min_dif = min(min_dif, que[0][0])

print(min_dif)
