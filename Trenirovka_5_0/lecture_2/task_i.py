# I. Пираты Баренцева моря
# Вася играет в настольную игру «Пираты Баренцева моря», которая посвящена морским битвам. Игровое поле представляет
# собой квадрат из N×N клеток, на котором расположено N кораблей (каждый корабль занимает одну клетку).
# Вася решил воспользоваться линейной тактикой, для этого ему необходимо выстроить все N кораблей в одном столбце.
# За один ход можно передвинуть один корабль в одну из четырёх соседних по стороне клеток. Номер столбца,
# в котором будут выстроены корабли, не важен. Определите минимальное количество ходов, необходимых для построения
# кораблей в одном столбце. В начале и процессе игры никакие два корабля не могут находиться в одной клетке.
# Формат ввода
# В первой строке входных данных задаётся число N (1≤N≤100).
# В каждой из следующих N строк задаются координаты корабля: сначала номер строки, затем номер столбц
# а (нумерация начинается с единицы).
# Формат вывода
# Выведите одно число — минимальное количество ходов, необходимое для построения.
# Пример
# Ввод	Вывод
# 3       3
# 1 2
# 3 3
# 1 1


def move_ships(col_num, ships):
    column = [0] * (n + 1)
    moved_ships = []
    for j in range(n):
        if ships[j][1] == col_num:
            column[ships[j][0]] = 1
        else:
            moved_ships.append(ships[j])
    moved_ships.sort()
    res = 0
    index = 0
    for z in range(1, n + 1):
        if column[z] == 0:
            ship = moved_ships[index]
            res += abs(col_num - ship[1]) + abs(z - ship[0])
            index += 1
    return res


n = int(input())
ships = []

for i in range(n):
    x, y = map(int, input().split())
    ships.append((x, y))

# col_num = round(sum([k[1] for k in ships]) / n)
# left = max(1, col_num - 2)
# right = min(n + 1, col_num + 3)
best_res = 100000
for m in range(1, n + 1):
    temp_res = move_ships(m, ships)
    if temp_res < best_res:
        best_res = temp_res
print(best_res)

