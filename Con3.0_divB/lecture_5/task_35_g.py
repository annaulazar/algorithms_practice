n = int(input())
adj_matrix = []

# ввод матрицы смежности
for i in range(n):
    adj_matrix.append(list(map(int, input().split())))

visited = [False] * n
cycle = []

def dfs(v, p):
    visited[v] = True
    for u in range(n):
        # проверяем, является ли вершина смежной с текущей
        if adj_matrix[v][u] == 1:
            # если вершина уже была посещена и не является предком текущей вершины, то цикл найден
            if visited[u] and u != p:
                # осуществляем обход цикла и сохраняем его вершины
                cycle.append(u)
                while v != u:
                    cycle.append(v)
                    v = parents[v]
                cycle.append(u)
                return True
            # иначе продолжаем обход
            elif not visited[u]:
                parents[u] = v
                if dfs(u, v):
                    return True
    return False

# запускаем DFS от всех вершин графа
for i in range(n):
    parents = [-1] * n
    if not visited[i]:
        if dfs(i, -1):
            break

# выводим результат
if len(cycle) > 0:
    print("YES")
    print(len(cycle))
    print(" ".join(str(c + 1) for c in cycle[::-1]))
else:
    print("NO")
