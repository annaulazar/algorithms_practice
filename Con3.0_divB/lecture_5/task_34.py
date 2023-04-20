import sys

sys.setrecursionlimit(1000000)

with open('input.txt') as f:
    v, e = map(int, f.readline().strip().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, f.readline().strip().split())
        graph[v1].append(v2)

visited = [0] * (v + 1)
isCicle = False
ans = []

def dfs(now):
    global isCicle
    visited[now] = 1
    for neib in graph[now]:
        if not visited[neib]:
            dfs(neib)
        elif visited[neib] == 1:
            isCicle = True
    visited[now] = 2
    ans.append(now)

for i in range(1, v + 1):
    if not visited[i]:
        dfs(i)
if isCicle:
    print(-1)
else:
    print(*ans[::-1])
