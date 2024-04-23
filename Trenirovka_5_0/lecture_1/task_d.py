# На шахматной доске стоят слоны и ладьи, необходимо посчитать, сколько клеток не бьется ни одной из фигур.
# Шахматная доска имеет размеры 8 на 8. Ладья бьет все клетки горизонтали и вертикали, проходящих через
# клетку, где она стоит, до первой встретившейся фигуры. Слон бьет все клетки обеих диагоналей,
# проходящих через клетку, где он стоит, до первой встретившейся фигуры.
# Формат ввода
# В первых восьми строках ввода описывается шахматная доска. Первые восемь символов каждой из этих строк
# описывают состояние соответствующей горизонтали: символ B (заглавная латинская буква) означает, что
# в клетке стоит слон, символ R — ладья, символ * — что клетка пуста. После описания горизонтали в строке
# могут идти пробелы, однако длина каждой строки не превышает 250 символов. После описания доски в файле
# могут быть пустые строки.
# Формат вывода
# Выведите количество пустых клеток, которые не бьются ни одной из фигур.


def for_rook(row, col):
    for x in range(row - 1, -1, -1):
        if table[x][col] != -1:
            table[x][col] = 0
        else:
            break
    for x in range(row + 1, 8):
        if table[x][col] != -1:
            table[x][col] = 0
        else:
            break
    for y in range(col - 1, -1, -1):
        if table[row][y] != -1:
            table[row][y] = 0
        else:
            break
    for y in range(col + 1, 8):
        if table[row][y] != -1:
            table[row][y] = 0
        else:
            break


def for_bishop(row, col):
    x, y = row - 1, col + 1
    while x >= 0 and y < 8:
        if table[x][y] != -1:
            table[x][y] = 0
            x -= 1
            y += 1
        else:
            break
    x, y = row + 1, col - 1
    while x < 8 and y >= 0:
        if table[x][y] != -1:
            table[x][y] = 0
            x += 1
            y -= 1
        else:
            break
    x, y = row - 1, col - 1
    while x >= 0 and y >= 0:
        if table[x][y] != -1:
            table[x][y] = 0
            x -= 1
            y -= 1
        else:
            break
    x, y = row + 1, col + 1
    while x < 8 and y < 8:
        if table[x][y] != -1:
            table[x][y] = 0
            x += 1
            y += 1
        else:
            break


rooks = []
bishops = []
table = [[1] * 8 for _ in range(8)]

for i in range(8):
    s = input().strip()
    for j in range(8):
        if s[j] == 'R':
            table[i][j] = -1
            rooks.append((i, j))
        elif s[j] == 'B':
            table[i][j] = -1
            bishops.append((i, j))

for rook in rooks:
    for_rook(*rook)
for bishop in bishops:
    for_bishop(*bishop)

res = 0
for k in range(8):
    res += sum((z for z in table[k] if z > 0))
print(res)
