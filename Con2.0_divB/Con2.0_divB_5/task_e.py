# Даны три массива целых чисел A,B,C и целое число S.
# Найдите такие i,j,k, что Ai+Bj+Ck=S.
# Формат ввода
# На первой строке число S (1≤S≤109). Следующие три строки содержат описание массивов A,B,C
# в одинаковом формате: первое число задает длину n соответствующего массива (1≤n≤15000),
# затем заданы n целых чисел от 1 до 109 — сам массив.
# Формат вывода
# Если таких i,j,k не существует, выведите единственное число −1. Иначе выведите
# на одной строке три числа — i,j,k. Элементы массивов нумеруются с нуля.
# Если ответов несколько, выведите лексикографически минимальный.

# Решение n2 со словарем для с, не проходит на больших тестах python10, но pypy проходит
s = int(input())
n_a, *a = [int(x) for x in input().split()]
n_b, *b = [int(x) for x in input().split()]
n_c, *c = [int(x) for x in input().split()]
c_dict = {}
for i in range(n_c):
    if c[i] not in c_dict:
        c_dict[c[i]] = i
    else:
        if i < c_dict[c[i]]:
            c_dict[c[i]] = i
res = False
for i in range(n_a):
    for j in range(n_b):
        t = s - a[i] - b[j]
        if t in c_dict:
            k = c_dict[t]
            res = True
            break
    if res:
        break
if res:
    print(i, j, k)
else:
    print(-1)

