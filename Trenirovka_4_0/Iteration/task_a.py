# По данному числу N (0 < N < 10) выведите все перестановки чисел от 1 до N
# в лексикографическом порядке.

# Решение с помощью модуля itertools, ф-ия permutations генерирует все перестановки
# import itertools
#
# n = int(input())
# for combination in itertools.permutations(range(1, n + 1)):
#     print(''.join(map(str, combination)))

# Решение с помощью рекурсивной функции, запуская ее на урезанном массиве без выбранного числа и накапливая результат
# def permute(s: list):
#     out = []
#     if len(s) == 1:
#         return s
#     else:
#         for i, let in enumerate(s):
#             for perm in permute(s[:i] + s[i + 1:]):
#                 out += [let + perm]
#     return out
#
# n = int(input())
# array = [str(x) for x in range(1, n + 1)]
# res = permute(array)
# print(*res)

# Решение с помощью рекурсивной функции, которая буквально совершает перестановки в массиве и
# распечатывая каждую перестановку (не получатся лексикографически)
def permutations(arr, curr_index=0):
    if curr_index == len(arr) - 1:
        print(''.join(arr))

    for i in range(curr_index, len(arr)):
        arr[curr_index], arr[i] = arr[i], arr[curr_index]
        permutations(arr, curr_index + 1)
        arr[curr_index], arr[i] = arr[i], arr[curr_index]


# Решение с помощью рекурсии, запуская на обрезанном массиве и накапливая строку комбинации, сразу печатая ее

def permutations2(arr, combination=''):
    if len(arr) == 0:
        print(combination)

    for i in range(len(arr)):
        new_combination = combination + arr[i]
        new_arr = arr[0:i] + arr[i + 1:]
        permutations2(new_arr, new_combination)

n = int(input())
array = [str(x) for x in range(1, n + 1)]
permutations2(array)
