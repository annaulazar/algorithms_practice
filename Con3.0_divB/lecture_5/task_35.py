v = int(input())
graph = [[] for _ in range(v + 1)]
for i in range(v):
    row = [int(x) for x in input().split()]
    for j in range(v):
        if row[j]:
            graph[i + 1].append(j + 1)

visited = [0] * (v + 1)
cicle = []

def dfs(now, parent):
    visited[now] = 1
    for neib in graph[now]:
        if not visited[neib]:
            prev[neib] = now
            if dfs(neib, now):
                return True
        elif visited[neib] == 1 and neib != parent:
            cicle.append(now)
            while prev[now] != neib:
                now = prev[now]
                cicle.append(now)
            cicle.append(neib)
            return True
    return False


for i in range(1, v + 1):
    prev = [0] * (v + 1)
    if not visited[i]:
        if dfs(i, 0):
            break


if len(cicle) > 0:
    print("YES")
    print(len(cicle))
    print(*cicle)
else:
    print("NO")
