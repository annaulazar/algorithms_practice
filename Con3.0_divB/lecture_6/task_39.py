from collections import deque

n = int(input())

table_3 = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        table_3[-1][i][j] = -2
for k in range(n):
    for i in range(n + 1):
        table_3[k][i][-1] = -2
    for j in range(n + 1):
        table_3[k][-1][j] = -2

start_x, start_y, start_z = 0, 0, 0
for k in range(n):
    input()
    for i in range(n):
        row = list(input())
        for j in range(n):
            if row[j] == '#':
                table_3[k][i][j] = -2
            elif row[j] == 'S':
                start_x, start_y, start_z = i, j, k

def bfs(x, y, z):
    deque_ = deque()
    step = 0
    table_3[z][x][y] = step
    deque_.append((x, y, z, step))
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while deque_:
        cur_x, cur_y, cur_z, cur_step = deque_.popleft()
        step = cur_step + 1
        for i in range(6):
            x = cur_x + dx[i]
            y = cur_y + dy[i]
            z = cur_z + dz[i]
            if table_3[z][x][y] == -1:
               table_3[z][x][y] = step
               deque_.append((x, y, z, step))

bfs(start_x, start_y, start_z)
res = n ** 3 + 1
for i in range(n):
    for j in range(n):
        if table_3[0][i][j] != -2 and table_3[0][i][j] != -1 and table_3[0][i][j] < res:
            res = table_3[0][i][j]

print(res)
