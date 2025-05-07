# Дан массив a из n целых чисел. Напишите программу, которая найдет число, которое встречается в
# массиве наибольшее число раз.
# Формат ввода
# В первой строке входных данных записано число n (1 ≤ n ≤ 300 000). Во второй строке записаны n
# целых чисел ai (0 ≤ ai ≤ 1 000 000 000).
# Формат вывода
# Выведите единственное число x, наибольшее из чисел, которое встречается в a максимальное количество раз.

n = int(input())
a = [int(x) for x in input().split()]
numbers = {}
for num in a:
    numbers[num] = numbers.get(num, 0) + 1
# res = [(k, v) for k, v in numbers.items()]
# res.sort(key=lambda x: (x[1], x[0]))
# print(res[-1][0])

t = max(numbers.values())
res = filter(lambda x: numbers[x] == t, numbers.keys())
print(max(res))
