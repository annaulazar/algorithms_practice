# Дан неориентированный граф. Требуется определить, есть ли в нем цикл, и, если есть, вывести его.
# Формат ввода
# В первой строке дано одно число n — количество вершин в графе ( 1 ≤ n ≤ 500 ). Далее в n строках задан
# сам граф матрицей смежности.
# Формат вывода
# Если в иcходном графе нет цикла, то выведите «NO». Иначе, в первой строке выведите «YES», во второй строке
# выведите число k — количество вершин в цикле, а в третьей строке выведите k различных чисел — номера вершин,
# которые принадлежат циклу в порядке обхода (обход можно начинать с любой вершины цикла). Если циклов
# несколько, то выведите любой.
# Пример 1
# Ввод	    Вывод
# 3           YES
# 0 1 1       3
# 1 0 1       3 2 1
# 1 1 0
# Пример 2
# Ввод	    Вывод
# 4           NO
# 0 0 1 0
# 0 0 0 1
# 1 0 0 0
# 0 1 0 0
# Пример 3
# Ввод	       Вывод
# 5             YES
# 0 1 0 0 0     3
# 1 0 0 0 0     5 4 3
# 0 0 0 1 1
# 0 0 1 0 1
# 0 0 1 1 0


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
