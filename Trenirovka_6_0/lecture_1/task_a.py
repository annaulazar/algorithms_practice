# Плот
# Посередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов.
# Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота
# имеет координаты (x1,y1), северо-восточный угол – координаты (x2,y2).
# Пловец находится в точке с координатами (x, y). Определите, к какой стороне плота (северной, южной, западной или
# восточной) или к какому углу плота (северо-западному, северо-восточному, юго-западному, юго-восточному) пловцу нужно
# плыть, чтобы как можно скорее добраться до плота.
# Формат ввода
# Программа получает на вход шесть чисел в следующем порядке: x1,y1 (координаты юго-западного угла плота),
# x2,y2 (координаты северо-восточного угла плота), x,y (координаты пловца). Все числа целые и по модулю не превосходят 100.
# Гарантируется, что x1<x2, y1<y2, координаты пловца находятся вне плота.
# Формат вывода
# Если пловцу следует плыть к северной стороне плота, программа должна вывести символ ”N”, к южной — символ ”S”,
# к западной — символ ”W”, к восточной — символ ”E”. Если пловцу следует плыть к углу плота, нужно вывести одну из
# следующих строк: ”NW”, ”NE”, ”SW”, ”SE”.
# Пример
# Ввод	Вывод
# -1      NW
# -2
# 5
# 3
# -4
# 6


y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())
if x <= x1:
    if y >= y2:
        print('NW')
    elif y <= y1:
        print('SW')
    else:
        print('W')
elif x >= x2:
    if y >= y2:
        print('NE')
    elif y <= y1:
        print('SE')
    else:
        print('E')
else:
    if y > y2:
        print('N')
    else:
        print('S')
