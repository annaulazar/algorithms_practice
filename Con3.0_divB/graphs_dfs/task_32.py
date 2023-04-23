# Дан неориентированный невзвешенный граф, состоящий из N вершин и M ребер. Необходимо посчитать количество
# его компонент связности и вывести их.
# Формат ввода
# Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках записаны
# по два числа i и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром.
# Формат вывода
# В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты
# связности в следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в
# произвольном порядке.
# Пример 1
# Ввод	Вывод
# 6 4     3
# 3 1     3
# 1 2     1 2 3
# 5 4     2
# 2 3     4 5
#         1
#         6
# Пример 2
# Ввод	Вывод
# 6 4     2
# 4 2     5
# 1 4     1 2 3 4 6
# 6 4     1
# 3 6     5


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
