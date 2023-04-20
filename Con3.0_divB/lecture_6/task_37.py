from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]
for i in range(v):
    row = [int(x) for x in input().split()]
    for j in range(v):
        if row[j]:
            graph[i + 1].append(j + 1)

visited = [-1] * (v + 1)
prev = [-1] * (v + 1)

def bfs(now):
    deque_ = deque()
    step = 0
    visited[now] = step
    deque_.append((now, step))
    while deque_:
        cur_vert, cur_step = deque_.popleft()
        step = cur_step + 1
        for neighb in graph[cur_vert]:
            if visited[neighb] == -1:
                visited[neighb] = step
                deque_.append((neighb, step))
                prev[neighb] = cur_vert


start, end = map(int, input().split())
bfs(start)
path = visited[end]
print(path)
if path > 0:
    res = [end]
    temp = prev[end]
    while temp != -1:
        res.append(temp)
        temp = prev[temp]
    print(*res[::-1])
