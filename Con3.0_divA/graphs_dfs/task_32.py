# Дан ориентированный граф, возможно, с петлями и кратными ребрами.
# Необходимо найти все вершины, из которых достижима первая вершина.
# Формат ввода
# В первой строке записаны два целых числа N (1 ≤ N ≤ 103) и M (0 ≤ M ≤ 5 * 105) — количество вершин и ребер
# в графе.
# В последующих M строках перечислены ребра — пары чисел, определяющие номера вершин, которые соединяют
# ребра (в порядке «откуда» и «куда» ведет ребро).
# Формат вывода
# Выведите все вершины, из которых достижима первая, в порядке возрастания их номеров.
# Пример
# Ввод	Вывод
# 4 5     1 2 3 4
# 2 2
# 4 3
# 2 3
# 3 1
# 2 4

import sys

sys.setrecursionlimit(1000000)

def dfs(graph, visited, now):
    visited[now] = 1
    for neib in graph[now]:
        if not visited[neib]:
            dfs(graph, visited, neib)


v, e = map(int, input().strip().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    v1, v2 = map(int, input().strip().split())
    graph[v2].append(v1)

visited = [0] * (v + 1)

dfs(graph, visited, 1)
answer = [index for index, value in enumerate(visited) if value]
print(*answer)
