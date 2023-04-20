import sys

sys.setrecursionlimit(1000000)

def dfs(graph, visited, now):
    visited[now] = True
    for neib in graph[now]:
        if not visited[neib]:
            dfs(graph, visited, neib)


with open('input.txt') as f:
    v, e = map(int, f.readline().strip().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, f.readline().strip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

visited = [0] * (v + 1)
dfs(graph, visited, 1)
res = [index for index, value in enumerate(visited) if value]
print(len(res))
print(*sorted(res))
