# D. Шахматная доска
# Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр.
# Требуется определить ее периметр.
# Формат ввода
# Сначала вводится число N (1 ≤ N ≤ 64) – количество выпиленных клеток. В следующих N строках вводятся
# координаты выпиленных клеток, разделенные пробелом (номер строки и столбца – числа от 1 до 8). Каждая
# выпиленная клетка указывается один раз.
# Формат вывода
# Выведите одно число – периметр выпиленной фигуры (сторона клетки равна единице).
# Пример 1
# Ввод	Вывод
# 3       8
# 1 1
# 1 2
# 2 1
# Пример 2
# Ввод	Вывод
# 1       4
# 8 8


table = [[0] * 10 for _ in range(10)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    table[x][y] = 1
dx = (0, -1, 0, 1)
dy = (-1, 0, 1, 0)
res = 0
for i in range(1, 9):
    for j in range(1, 9):
        if table[i][j] == 1:
            for k in range(4):
                if table[i + dx[k]][j + dy[k]] == 0:
                    res += 1
print(res)
