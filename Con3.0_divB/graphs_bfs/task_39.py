# Пещера представлена кубом, разбитым на N частей по каждому измерению (то есть на N3 кубических клеток).
# Каждая клетка может быть или пустой, или полностью заполненной камнем. Исходя из положения спелеолога
# в пещере, требуется найти, какое минимальное количество перемещений по клеткам ему требуется, чтобы
# выбраться на поверхность. Переходить из клетки в клетку можно, только если они обе свободны и имеют
# общую грань.
# Формат ввода
# В первой строке содержится число N (1 ≤ N ≤ 30). Далее следует N блоков. Блок состоит из пустой строки
# и N строк по N символов: # - обозначает клетку, заполненную камнями, точка - свободную клетку. Начальное
# положение спелеолога обозначено заглавной буквой S. Первый блок представляет верхний уровень пещеры,
# достижение любой свободной его клетки означает выход на поверхность. Выход на поверхность всегда возможен.
# Формат вывода
# Вывести одно число - длину пути до поверхности.
# Пример
# Ввод	Вывод
# 3       6
# ###
# ###
# .##
#
# .#.
# .#S
# .#.
#
# ###
# ...
# ###


from collections import deque

n = int(input())

table_3 = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        table_3[-1][i][j] = -2
for k in range(n):
    for i in range(n + 1):
        table_3[k][i][-1] = -2
    for j in range(n + 1):
        table_3[k][-1][j] = -2

start_x, start_y, start_z = 0, 0, 0
for k in range(n):
    input()
    for i in range(n):
        row = list(input())
        for j in range(n):
            if row[j] == '#':
                table_3[k][i][j] = -2
            elif row[j] == 'S':
                start_x, start_y, start_z = i, j, k

def bfs(x, y, z):
    deque_ = deque()
    step = 0
    table_3[z][x][y] = step
    deque_.append((x, y, z, step))
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while deque_:
        cur_x, cur_y, cur_z, cur_step = deque_.popleft()
        step = cur_step + 1
        for i in range(6):
            x = cur_x + dx[i]
            y = cur_y + dy[i]
            z = cur_z + dz[i]
            if table_3[z][x][y] == -1:
               table_3[z][x][y] = step
               deque_.append((x, y, z, step))

bfs(start_x, start_y, start_z)
res = n ** 3 + 1
for i in range(n):
    for j in range(n):
        if table_3[0][i][j] != -2 and table_3[0][i][j] != -1 and table_3[0][i][j] < res:
            res = table_3[0][i][j]

print(res)
