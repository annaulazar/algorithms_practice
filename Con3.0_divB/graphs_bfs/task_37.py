# В неориентированном графе требуется найти минимальный путь между двумя вершинами.
# Формат ввода
# Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица
# смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин –
# начальной и конечной.
# Формат вывода
# Выведите сначала L – длину кратчайшего пути (количество ребер, которые нужно пройти), а потом сам
# путь. Если путь имеет длину 0, то его выводить не нужно, достаточно вывести длину.
# Необходимо вывести путь (номера всех вершин в правильном порядке). Если пути нет, нужно вывести -1.
# Пример
# Ввод	                 Вывод
# 10                       2
# 0 1 0 0 0 0 0 0 0 0      5 2 4
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


from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]
for i in range(v):
    row = [int(x) for x in input().split()]
    for j in range(v):
        if row[j]:
            graph[i + 1].append(j + 1)

visited = [-1] * (v + 1)
prev = [-1] * (v + 1)

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
                prev[neighb] = cur_vert


start, end = map(int, input().split())
bfs(start)
path = visited[end]
print(path)
if path > 0:
    res = [end]
    temp = prev[end]
    while temp != -1:
        res.append(temp)
        temp = prev[temp]
    print(*res[::-1])
