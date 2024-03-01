# Взвешенный неориентированный граф без петель задан матрицей смежности. Распределите вершины по двум долям так,
# чтобы сумма весов рёбер, соединяющих вершины из разных долей, была максимальна.
# Формат ввода
# Вводится число N (2 ≤ N ≤ 20) — количество вершин в графе.
# В следующих N строках, содержащих по N целых чисел от 0 до 1000, задаётся матрица смежности. 0 означает
# отсутствие ребра.
# Формат вывода
# В первой строке выведите суммарный вес рёбер, соединяющих вершины из разных долей.
# Во второй строке выведите N чисел 1 или 2 — номера долей для каждой из вершин графа.
# Пример 1
# Ввод	Вывод
# 2       1
# 0 1     2 1
# 1 0
# Пример 2
# Ввод	 Вывод
# 3        4
# 0 1 2    2 2 1
# 1 0 2
# 2 2 0
# Пример 3
# Ввод	    Вывод
# 4           26
# 0 10 3 0    2 1 2 1
# 10 0 7 2
# 3 7 0 9
# 0 2 9 0

def get_sum_between_parts(table: list[list], marks: list) -> int:
    res = 0
    for i in range(n):
        for neighbor in table[i]:
            if marks[i] != marks[neighbor[0]]:
                res += neighbor[1]
    return res // 2

# Решение верное, но не проходит по времени на больших тестах. Как оптимизировать, не пойму
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    row = [int(x) for x in input().split()]
    for j in range(n):
        if row[j]:
            graph[i].append((j, row[j]))
best_colors = [0] * n
best_sum = 0

for k in range(1, 2**(n - 1)):
    num_list = list(map(int, list(bin(k)[2:])))
    z = len(num_list)
    colors = [0] + [0] * (n - z - 1) + num_list
    summa = get_sum_between_parts(graph, colors)
    if summa > best_sum:
        best_sum = summa
        best_colors = colors

print(best_sum)
for color in best_colors:
    print(2 - color, end=' ')
