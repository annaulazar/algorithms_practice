import sys

sys.setrecursionlimit(1000000)

def dfs(graph, visited, now, comp):
    visited[now] = comp
    for neib in graph[now]:
        if not visited[neib]:
            dfs(graph, visited, neib, comp)


with open('input.txt') as f:
    v, e = map(int, f.readline().strip().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, f.readline().strip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

visited = [0] * (v + 1)
comp = 1
for i in range(1, v + 1):
    if not visited[i]:
        dfs(graph, visited, i, comp)
        comp += 1
print(comp - 1)
comp_dict = {}
for j in range(1, v + 1):
    comp_dict[visited[j]] = comp_dict.get(visited[j], []) + [j]
for key in sorted(comp_dict.keys()):
    print(len(comp_dict[key]))
    print(*comp_dict[key])
