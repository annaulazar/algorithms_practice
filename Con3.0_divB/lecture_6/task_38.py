from collections import deque

n, m, s, t, q = map(int, input().split())
table = [[-1] * (m + 3) for _ in range(n + 3)]
for i in range(n + 3):
    table[i][0], table[i][-2], table[i][-1] = -2, -2, -2
for j in range(m + 3):
    table[0][j], table[-2][j], table[-1][j] = -2, -2, -2


def bfs(x, y):
    deque_ = deque()
    step = 0
    table[x][y] = step
    deque_.append((x, y, step))
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    while deque_:
        cur_x, cur_y, cur_step = deque_.popleft()
        step = cur_step + 1
        for i in range(8):
            x = cur_x + dx[i]
            y = cur_y + dy[i]
            if table[x][y] == -1:
               table[x][y] = step
               deque_.append((x, y, step))

bfs(s, t)
res = 0
for _ in range(q):
    x, y = map(int, input().split())
    temp = table[x][y]
    if temp == -1:
        res = -1
        break
    else:
        res += temp
print(res)
