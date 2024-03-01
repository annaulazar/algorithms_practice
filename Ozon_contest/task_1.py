# Вы участвуете в разработке подсистемы проверки поля для игры <<Морской бой>>. Вам требуется написать проверку
# корректности количества кораблей на поле, учитывая их размеры. Напомним, что на поле должны быть: четыре однопалубных
# корабля, три двухпалубных корабля, два трёхпалубных корабля, один четырёхпалубный корабль.
# Вам заданы 10 целых чисел от 1 до 4. Проверьте, что заданные размеры соответствуют требованиям выше.
# Пример теста 1
# Входные данные
# 5
# 2 1 3 1 2 3 1 1 4 2
# 1 1 1 2 2 2 3 3 3 4
# 1 1 1 1 2 2 2 3 3 4
# 4 3 3 2 2 2 1 1 1 1
# 4 4 4 4 4 4 4 4 4 4
# Выходные данные
# YES
# NO
# YES
# YES
# NO


sample = {1: 4, 2: 3, 3: 2, 4: 1}
n = int(input())
for _ in range(n):
    ships = [int(x) for x in input().split()]
    ship_dict = {}
    for number in ships:
        ship_dict[number] = ship_dict.get(number, 0) + 1
    if ship_dict == sample:
        print('YES')
    else:
        print('NO')