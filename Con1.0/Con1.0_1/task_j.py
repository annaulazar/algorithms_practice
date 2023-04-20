# Даны числа a, b, c, d, e, f. Решите систему линейных уравнений

from random import randint, choice
a, b, c, d, e, f = (float(input()) for _ in range(6))

def lin_sys(a, b, c, d, e, f):
    delta = a * d - c * b
    delta_x = e * d - f * b
    delta_y = a * f - c * e

    if delta != 0:
        x = round(delta_x / delta, 5)
        y = round(delta_y / delta, 5)
        print(2, x, y)
    else:
        if delta_x == 0 and delta_y == 0:
            if a == 0 and b == 0 and c == 0 and d == 0:
                print(0 if e != 0 or f != 0 else 5)
            else:
                if a == 0 and c == 0:
                    y = round(e / b, 5) if b != 0 else round(f / d, 5)
                    print(4, y)
                else:
                    if b == 0 and d == 0:
                        x = round(e / a, 5) if a != 0 else round(f / c, 5)
                        print(3, x)
                    else:
                        if b != 0:
                            n = round(e / b, 5)
                            k = round(-a / b, 5)
                        else:
                            n = round(f / d, 5)
                            k = round(-c / d, 5)
                        print(1, k, n)
        else:
            print(0)

lin_sys(a, b, c, d, e, f)

# while True:
#     n = 6
#     rand_list = []
#     for i in range(n):
#         rand_list.append(choice((0, 0, randint(1, 9))))
#     try:
#         lin_sys(*rand_list)
#     except Exception as e:
#         print(rand_list)
#         print(e)
#         break
