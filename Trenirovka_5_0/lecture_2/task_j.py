# J. Два прямоугольника
# Недавно один известный художник-абстракционист произвел на свет новый шедевр — картину «Два черных непересекающихся
# прямоугольника». Картина представляет собой прямоугольник m× n, разбитый на квадраты 1× 1, некоторые из которых
# закрашены любимым цветом автора — черным. Федя — не любитель абстрактных картин, однако ему стало интересно,
# действительно ли на картине изображены два непересекающихся прямоугольника. Помогите ему это узнать.
# Прямоугольники не пересекаются в том смысле, что они не имеют общих клеток.
# Формат ввода
# Первая строка входного файла содержит числа m и n (1 ≤ m, n ≤ 200). Следующие m строк содержат описание рисунка.
# Каждая строка содержит ровно n символов. Символ «.» обозначает пустой квадрат, а символ «#» — закрашенный.
# Формат вывода
# Если рисунок можно представить как два непересекающихся прямоугольника, выведите в первой строке «YES», а в
# следующих m строках выведите рисунок в том же виде, в каком он задан во входном файле, заменив квадраты,
# соответствующие первому прямоугольнику на символ «a», а второму — на символ «b». Если решений несколько, выведите любое.
# Если же этого сделать нельзя, выведите в выходной файл «NO».
# Пример 1
# Ввод	Вывод
# 2 1     NO
# #
# .
# Пример 2
# Ввод	Вывод
# 2 2     YES
# ..      ..
# ##      ab

# Не верное, не проходит все тесты
def print_table(table):
    for row in table:
        print(''.join(row))


n, m = map(int, input().split())
table = [[""] * m for _ in range(n)]
for i in range(n):
    row = input().strip()
    for j in range(m):
        table[i][j] = row[j]

flag_a = False
flag_b = False
t_a, b_a, l_a, r_a = -1, -1, -1, -1
t_b, b_b, l_b, r_b = -1, -1, -1, -1
count_wrong = 0
for i in range(n):
    for j in range(m):
        if table[i][j] == '#':
            if not flag_a:
                table[i][j] = 'a'
                l_a = j
                t_a = i
                flag_a = True
            elif flag_a and r_a == -1 or (l_a <= j <= r_a and not(flag_b and r_b == -1)):
                table[i][j] = 'a'
            elif (j < l_a or j > r_a) and not flag_b:
                table[i][j] = 'b'
                l_b = j
                t_b = i
                flag_b = True
            elif flag_b and r_b == -1 or l_b <= j <= r_b:
                table[i][j] = 'b'
            else:
                count_wrong += 1
            if j == m - 1:
                if flag_a and r_a == -1:
                    r_a = j
                elif flag_b and r_b == -1:
                    r_b = j
            if i == n - 1:
                if flag_a and b_a == -1:
                    b_a = i
                elif flag_b and b_b == -1:
                    b_b = i
        else:
            if j > 0 and table[i][j - 1] == 'a' and r_a == -1:
                r_a = j - 1
            elif i > 0 and table[i - 1][j] == 'a' and b_a == -1:
                b_a = i - 1
            elif l_a <= j <= r_a and b_a == -1:
                b_a = i - 1
                if not flag_b:
                    flag_b = True
                    l_b = l_a
                    t_b = i
                    for k in range(l_a, j + 1):
                        table[i][k] = 'b'
                elif flag_b and r_b == -1:
                    for k in range(l_a, j + 1):
                        table[i][k] = 'b'
            elif j > 0 and table[i][j - 1] == 'b' and r_b == -1:
                r_b = j
            elif i > 0 and table[i - 1][j] == 'b' and b_a == -1:
                b_a = j

if not flag_b:
    if r_a - l_a == 0 and b_a - t_a == 0:
        print('NO')
    else:
        if r_a - l_a > 0:
            for k in range(t_a, b_a + 1):
                table[k][r_a] = 'b'
        else:
            table[b_a][l_a] = 'b'
        print('YES')
        print_table(table)
else:
    if count_wrong > 0:
        print('NO')
    else:
        print('YES')
        print_table(table)


