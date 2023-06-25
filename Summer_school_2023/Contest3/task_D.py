# На прямой расположены стойла, в которые необходимо расставить коров так, чтобы минимальное расcтояние между
# коровами было как можно больше.
# В первой строке вводятся числа N (2 < N < 10001) – количество стойл и K (1 < K < N) – количество коров.
# Во второй строке задаются N натуральных чисел в порядке возрастания – координаты стойл (координаты
# не превосходят 109)
# Выведите одно число – наибольшее возможное допустимое расстояние.

n, k = (int(x) for x in input().split())
stoila = [int(i) for i in input().split()]


def check(dist, count, params):
    res = 1
    current = params[0]
    for param in params:
        if param - current >= dist:
            res += 1
            current = param
    return res >= count


l = 0
r = stoila[-1]
while l < r:
    m = (l + r + 1) // 2
    if check(m, k, stoila):
        l = m
    else:
        r = m - 1
print(l)
