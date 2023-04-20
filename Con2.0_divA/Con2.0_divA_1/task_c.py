# Напишите программу, которая по изображению поля для игры в «Крестики-нолики» определит, могла ли
# такая ситуация возникнуть в результате игры с соблюдением всех правил.
# Формат ввода
# Вводится три строки по три числа в каждой, описывающих игровое поле. Число 0 обозначает пустую клетку,
# 1 – крестик, 2 – нолик. Числа в строке разделяются пробелами.

pole = []
for _ in range(3):
    pole.extend([int(x) for x in input().split()])
x_o = sum([pole[i] == 1 for i in range(9)]) - sum([pole[i] == 2 for i in range(9)])
flagX, flag0 = 0, 0
if 0 <= x_o <= 1:
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for var in win:
        if pole[var[0]] == pole[var[1]] == pole[var[2]] == 1:
            flagX += 1
        if pole[var[0]] == pole[var[1]] == pole[var[2]] == 2:
            flag0 += 1
    if flagX in (1, 2) and flag0 == 0 and x_o == 1:
        print('YES')
    elif flag0 in (1, 2) and flagX == 0 and x_o == 0:
        print('YES')
    elif flagX == 0 and flag0 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
