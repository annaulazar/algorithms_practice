# Результаты контеста
# Чтобы оценить качество обучения программированию, в каждой группы студентов подсчитывается один параметр
# — суммарное количество решенных студентами задач.
# Известно, что в первой группе суммарное количество решенных на контесте задач равно a, а во второй — b.
# Всего на контесте было предложено n задач, а также известно, что каждый студент решил не менее одной
# (и не более n) задач.
# По заданным a, b и n определите, могло ли в первой группе быть строго больше студентов, чем во второй.
# Формат ввода
# Вводятся три целых числа a, b, n (1 ≤ a, b, n ≤ 10000).
# Формат вывода
# Выведите "Yes" если в первой группе могло быть строго больше студентов, чем во второй, и "No"
# в противном случае.
# Пример 1
# Ввод	Вывод
# 60      Yes
# 30
# 4
# Пример 2
# Ввод	Вывод
# 30      No
# 30
# 1
# Пример 3
# Ввод	Вывод
# 30      No
# 150
# 4

a = int(input())
b = int(input())
n = int(input())
b_min = b // n + bool(b % n)
if a > b_min:
    print('Yes')
else:
    print('No')
