# A. Угадай число - 2
# Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого она называет
# некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное
# или NO в противном случае. После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала
# и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.
# Август и Беатриса продолжают играть в игру, но Август начал жульничать. На каждый из вопросов Беатрисы он выбирает
# такой вариант ответа YES или NO, чтобы множество возможных задуманных чисел оставалось как можно больше.
# Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2, то Август ответит NO,
# а если Беатриса спросит про 1, 2, 3, то Август ответит YES. Если же Бетриса в своем вопросе перечисляет ровно
# половину из задуманных чисел, то Август из вредности всегда отвечает NO. Наконец, Август при ответе учитывает
# все предыдущие вопросы Беатрисы и свои ответы на них, то есть множество возможных задуманных чисел уменьшается.
# Формат ввода
# Вам дана последовательность вопросов Беатрисы. Приведите ответы Августа на них. Первая строка входных данных
# содержит число n — наибольшее число, которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы.
# Каждая строка представляет собой набор чисел, разделенных пробелами. Последняя строка входных данных содержит
# одно слово HELP.
# Формат вывода
# Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос. После этого выведите (через пробел, в порядке
# возрастания) все числа, которые мог загадать Август после ответа на все вопросы Беатрисы.
# Пример 1
# Ввод	      Вывод
# 10            NO
# 1 2 3 4 5     YES
# 2 4 6 8 10    6 8 10
# HELP


import sys


def fast_input():
    return sys.stdin.readline().rstrip("\r\n")


n = int(fast_input())
nums = set(range(1, n + 1))
qwest = fast_input()
answers = []
q_set = set(map(int, qwest.split()))
if len(q_set) > len(nums) / 2:
    answers.append('YES')
    nums = q_set
else:
    answers.append('NO')
    nums.difference_update(q_set)
qwest = fast_input()
while qwest != 'HELP':
    inter_set = nums.intersection(set(map(int, qwest.split())))
    if len(inter_set) > len(nums) / 2:
        answers.append('YES')
        nums = inter_set
    else:
        answers.append('NO')
        nums.difference_update(inter_set)
    qwest = fast_input()
print('\n'.join(answers))
print(*sorted(nums))
