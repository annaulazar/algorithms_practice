# B. Ни больше ни меньше
# Дан массив целых положительных чисел a длины n. Разбейте его на минимально возможное количество отрезков,
# чтобы каждое число было не меньше длины отрезка, которому оно принадлежит. Длиной отрезка считается
# количество чисел в нём.
# Разбиение массива на отрезки считается корректным, если каждый элемент принадлежит ровно одному отрезку.


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    res = []
    temp = 0
    temp_min = 1000000
    for number in nums:
        if min(temp_min, number) >= temp + 1:
            temp += 1
            temp_min = min(temp_min, number)
        else:
            res.append(temp)
            temp = 1
            temp_min = number
    res.append(temp)
    print(len(res))
    print(*res)
