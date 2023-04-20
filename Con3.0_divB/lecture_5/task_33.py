import sys

sys.setrecursionlimit(1000000)


with open('input.txt') as f:
    v, e = map(int, f.readline().strip().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, f.readline().strip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)


color = [0] * (v + 1)
isBipart = 'YES'

def dfs(now):
    global isBipart
    for neib in graph[now]:
        if color[neib] == 0:
            color[neib] = 3 - color[now]
            dfs(neib)
        elif color[neib] == color[now]:
            isBipart = 'NO'


for i in range(1, v + 1):
    if color[i] == 0:
        color[i] = 1
        dfs(i)
print(isBipart)
