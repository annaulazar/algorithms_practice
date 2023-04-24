# В неориентированном графе требуется найти длину минимального пути между двумя вершинами.
# Формат ввода
# Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица
# смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин –
# начальной и конечной.
# Формат вывода
# Выведите L – длину кратчайшего пути (количество ребер, которые нужно пройти).
# Если пути нет, нужно вывести -1.
# Пример 1
# Ввод	              Вывод
# 10                    2
# 0 1 0 0 0 0 0 0 0 0
# 1 0 0 1 1 0 1 0 0 0
# 0 0 0 0 1 0 0 0 1 0
# 0 1 0 0 0 0 1 0 0 0
# 0 1 1 0 0 0 0 0 0 1
# 0 0 0 0 0 0 1 0 0 1
# 0 1 0 1 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0
# 0 0 1 0 0 0 0 1 0 0
# 0 0 0 0 1 1 0 0 0 0
# 5 4
# Пример 2
# Ввод	      Вывод
# 5             3
# 0 1 0 0 1
# 1 0 1 0 0
# 0 1 0 0 0
# 0 0 0 0 0
# 1 0 0 0 0
# 3 5


from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]
for i in range(v):
    row = [int(x) for x in input().split()]
    for j in range(v):
        if row[j]:
            graph[i + 1].append(j + 1)

visited = [-1] * (v + 1)


def bfs(now):
    deque_ = deque()
    step = 0
    visited[now] = step
    deque_.append((now, step))
    while deque_:
        cur_vert, cur_step = deque_.popleft()
        step = cur_step + 1
        for neighb in graph[cur_vert]:
            if visited[neighb] == -1:
               visited[neighb] = step
               deque_.append((neighb, step))


start, end = map(int, input().split())
bfs(start)
print(visited[end])
