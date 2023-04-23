from collections import deque

n = int(input())
m = int(input())
lines = [set() for _ in range(m + 1)]
for i in range(1, m + 1):
    p, *s = [int(x) for x in input().split()]
    lines[i] = set(s)

graph = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(i + 1, m + 1):
        if lines[i] & lines[j]:
            graph[i].append(j)
            graph[j].append(i)

stations = [[] for _ in range(n + 1)]
for i in range(1, m + 1):
    for station in lines[i]:
        stations[station].append(i)

visited = [-1] * (m + 1)


def bfs(start):
    deque_ = deque()
    step = 0
    for line in stations[start]:
        visited[line] = step
        deque_.append((line, step))
    while deque_:
        cur_line, cur_step = deque_.popleft()
        step = cur_step + 1
        for neighb in graph[cur_line]:
            if visited[neighb] == -1:
               visited[neighb] = step
               deque_.append((neighb, step))

start, end = map(int, input().split())
bfs(start)
res = visited[stations[end][0]]
for line in stations[end]:
    if visited[line] < res and visited[line] != -1:
        res = visited[line]
print(res)
