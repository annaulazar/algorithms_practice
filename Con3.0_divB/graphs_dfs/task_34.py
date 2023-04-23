# Дан ориентированный граф. Необходимо построить топологическую сортировку.
# Формат ввода
# В первой строке входного файла два натуральных числа N и M (1 ≤ N, M ≤ 100 000) — количество вершин
# и рёбер в графе соответственно. Далее в M строках перечислены рёбра графа. Каждое ребро задаётся парой
# чисел — номерами начальной и конечной вершин соответственно.
# Формат вывода
# Выведите любую топологическую сортировку графа в виде последовательности номеров вершин (перестановка чисел
# от 1 до N). Если топологическую сортировку графа построить невозможно, выведите -1.
# Пример
# Ввод	Вывод
# 6 6     4 6 3 1 2 5
# 1 2
# 3 2
# 4 2
# 2 5
# 6 5
# 4 6


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
