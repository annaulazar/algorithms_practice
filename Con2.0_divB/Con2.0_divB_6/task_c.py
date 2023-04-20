# Дано кубическое уравнение ax3+bx2+cx+d=0 (a≠0). Известно, что у этого уравнения есть ровно один
# корень. Требуется его найти.
# Формат ввода
# Во входном файле через пробел записаны четыре целых числа: -1000 <= a, b, c, d <= 10000.
# Формат вывода
# Выведите единственный корень уравнения с точностью не менее 5 знаков после десятичной точки.


def func3(x):
    return a * x**3 + b * x**2 + c * x + d


def lbinpoisk(l, r, eps):
    while l + eps < r:
        m = (l + r) / 2
        if func3(m) >= 0:
            r = m
        else:
            l = m
    return l


def rbinpoisk(l, r, eps):
    while l + eps < r:
        m = (l + r) / 2
        if func3(m) <= 0:
            r = m
        else:
            l = m
    return l

a, b, c, d = [int(x) for x in input().split()]
if func3(100000) > func3(-100000):
    print(lbinpoisk(-100000, 100000, 0.00000001))
else:
    print(rbinpoisk(-100000, 100000, 0.00000001))
