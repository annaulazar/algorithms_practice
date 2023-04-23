# Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить компоненту связности,
# содержащую первую вершину.
# Формат ввода
# В первой строке записаны два целых числа N (1 ≤ N ≤ 103) и M (0 ≤ M ≤ 5 * 105) — количество вершин и
# ребер в графе. В последующих M строках перечислены ребра — пары чисел, определяющие номера вершин,
# которые соединяют ребра.
# Формат вывода
# В первую строку выходного файла выведите число K — количество вершин в компоненте связности. Во вторую
# строку выведите K целых чисел — вершины компоненты связности, перечисленные в порядке возрастания номеров.
# Пример
# Ввод	Вывод
# 4 5     4
# 2 2     1 2 3 4
# 3 4
# 2 3
# 1 3
# 2 4


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
