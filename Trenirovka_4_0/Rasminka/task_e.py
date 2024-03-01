# Средний уровень.
# В группе учатся n студентов, каждый из которых имеет свой рейтинг ai. Им нужно выбрать старосту;
# для этого студенты хотят выбрать старосту таким образом чтобы суммарный уровень недовольства группы
# был минимальный. Если выбрать j-го старостой, то уровень недовольства i-го студента равен ∣∣ai−aj∣∣.
# Например, если в группе есть три студента с рейтингами 1, 3 и 4 и в качестве старосты выбирают второго,
# то уровень недовольства группы будет равен|1−3|+|3−3|+|4−3|=3.
# Вычислите уровень недовольства группы при выборе каждого из студентов старостой.
# Формат ввода
# В первой строке дано единственное целое число n (1≤n≤105)  — количество студентов в группе.
# Во второй строке даны n целых чисел a1,a2,…,an, идущих по неубыванию (0≤a1≤a2≤…≤an≤104)  — рейтинги студентов.
# Формат вывода
# Выведите n чисел через пробел,i-е из которых будет обозначать уровень недовольства группы при выборе
# i-го студента старостой.
# Пример 1
# Ввод	   Вывод
# 3          5 3 4
# 1 3 4
# Пример 2
# Ввод	        Вывод
# 5               28 16 15 17 32
# 3 7 8 10 15

n = int(input())
a = [int(x) for x in input().split()]
S0 = 0
for i in range(n):
    S0 += a[i] - a[0]
res = [0] * n
res[0] = S0
for i in range(1, n):
    delta = a[i] - a[i - 1]
    res[i] = res[i-1] + delta * i - delta * (n - i)
print(*res)