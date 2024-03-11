# Решить в целых числах уравнение ( ax + b ) : ( cx + d ) = 0
# Вводятся 4 числа: a, b, c и d; c и d не равны нулю одновременно.

a, b, c, d = (int(input()) for _ in range(4))
t = 0
if c != 0:
    t = -d / c
if a == 0:
    if b != 0:
        print('NO')
    else:
        print('INF')
else:
    x = -b / a
    if abs(x - t) > 0.001 and abs(round(x) - x) < 0.001:
        print(round(x))
    else:
        print('NO')
