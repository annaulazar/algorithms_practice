'''Человек x не приглашает на день рождения человека y если выполнено хотя бы одно из условий:
- (Возраст человека y) <= 0.5 * (Возраст человека x) + 7
- (Возраст человека y) > (Возраст человека x)
- (Возраст человека y) > 100 и одновременно с этим (Возраст человека x) < 100
Во всех остальных случаях человек x приглашает человека y на день рождения.
Определите суммарное количество приглашений на день рождения.
В первой строке вводится число n (1 ≤ n ≤ 100000).
Во второй строке вводится n чисел — возраст людей. Возраст находится в промежутке от 1 до 120.'''

import random
# мое решение не верное, так как не правильно поняла условия
def my_f(ages, n):
    ages.sort(key=lambda x: -x)
    invites = 0
    last = 0
    for first in range(n-1):
        equal = first
        while equal < n - 1 and ages[equal + 1] == ages[first]:
            equal += 1
        invites += equal - first
        while last < n - 1 and ages[last + 1] > ages[first] * 0.5 + 7:
            last += 1
        if last >= first:
            invites += last - first
    return invites


def t_f(ages, n):
    ages.sort()
    left = 0
    right = 0
    ans = 0
    for i in range(n):
        while left < n and ages[left] <= 0.5 * ages[i] + 7:
            left += 1
        while right < n and ages[right] <= ages[i]:
            right += 1
        if right > left + 1:
            ans += right - left - 1
    return ans



#n = int(input())
#ages = [int(i) for i in input().split()]
#my_res = my_f(ages, n)
#t_res = t_f(ages, n)
#print(my_res, t_res)

while True:
    rand_list = [random.randint(1, 120) for _ in range(5)]
    my_res = my_f(rand_list, 5)
    t_res = t_f(rand_list, 5)
    if my_res != t_res:
        print(rand_list)
        print(my_res, t_res)
        break

