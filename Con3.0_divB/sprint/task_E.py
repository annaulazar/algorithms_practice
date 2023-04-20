H, W = map(int, input().split())
graph = [[-1] * (W + 2) for _ in range(H + 2)]
for i in range(H + 2):
    graph[i][0] = -2
    graph[i][-1] = -2
for j in range(W + 2):
    graph[0][j] = -2
    graph[-1][j] = -2
for i in range(1, H + 1):
    row = [' '] + list(input())
    for j in range(1, W + 1):
        if row[j] == 'X':
            graph[i][j] = -2


def bfs(x, y):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    step = 1
    steps = [[] for _ in range(H * W)]
    graph[y][x] = step
    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if graph[new_y][new_x] == -1:
            steps[step].append((new_x, new_y, i))
            graph[new_y][new_x] = step
    for j in range(1, len(steps)):
        # step = j
        # for vert in steps[j]:
        #     x, y, dir = vert
        #     new_x = x + dx[dir]
        #     new_y = y + dy[dir]
        #     if graph[new_y][new_x] == -1:
        #         steps[j].append((new_x, new_y, dir))
        #         graph[new_y][new_x] = step
        # step = j + 1
        for vert in steps[j]:
            x, y, dir = vert
            for i in range(8):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if i == dir:
                    step = j
                else:
                    step = j + 1
                if graph[new_y][new_x] == -1 or graph[new_y][new_x] > step:
                    steps[step].append((new_x, new_y, i))
                    graph[new_y][new_x] = step


start_x, start_y = map(int, input().split())
start_y = H + 1 - start_y
end_x, end_y = map(int, input().split())
end_y = H + 1 - end_y
bfs(start_x, start_y)
print(graph[end_y][end_x])
