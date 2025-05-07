from itertools import permutations
from random import randint, choice


def count_vasya_res(string):
    res = 0
    for i in range(len(string)):
        if i % 2 == 0 and string[i] == 'S':
            res += 1
    return res


def slow(tasks: []):
    res = 0
    for perm in permutations(tasks):
        flow = ''.join(perm)
        res = max(res, count_vasya_res(flow))
    return res

# tasks = ['SSSSSS', 'SSSSSS', 'SSSDS', 'SSS', 'SSD', 'SD']
# tasks1 = ['DSD', 'SS', 'DD', 'SDD']
# # print(slow(tasks))
# print(slow(tasks1))


def count_good_days(string: str) -> (int, int): # (кол-во хороших дней, если начинает Вася, если начинает Маша)
    v, m = 0, 0
    for i in range(len(string)):
        if i % 2 and string[i] == 'S':
            m += 1
        elif i % 2 == 0 and string[i] == 'S':
            v += 1
    return v, m


def fast(n, tasks_: []):
    tasks = {}
    best_if_vasya_start = []
    best_if_masha_start = []
    neutral = []

    res = 0
    for task in tasks_:
        s1, s2 = count_good_days(task)
        if s1 > s2:
            best_if_vasya_start.append(task)
        elif s1 < s2:
            best_if_masha_start.append(task)
        else:
            if len(task) % 2 == 0:
                res += s1
                n -= 1
            else:
                neutral.append(task)
        tasks[task] = (s1, s2)

    best_if_vasya_start.sort(key=lambda x: (len(x) % 2, -(tasks[x][0] - tasks[x][1])))
    best_if_masha_start.sort(key=lambda x: (len(x) % 2, -(tasks[x][1] - tasks[x][0])))
    cnt_v = len(best_if_vasya_start)
    cnt_m = len(best_if_masha_start)
    cnt_n = len(neutral)

    vasya_pointer = 0
    masha_pointer = 0
    neutral_pointer = 0
    day = 0
    while n > 0:
        if day % 2 == 0:
            if vasya_pointer < cnt_v:
                task = best_if_vasya_start[vasya_pointer]
                vasya_pointer += 1
            elif neutral_pointer < cnt_n:
                task = neutral[neutral_pointer]
                neutral_pointer += 1
            else:
                task = best_if_masha_start[cnt_v - vasya_pointer - 1]
                vasya_pointer += 1
            res += tasks[task][0]
            day += len(task)
            n -= 1
        else:
            if masha_pointer < cnt_m:
                task = best_if_masha_start[masha_pointer]
                masha_pointer += 1
            elif neutral_pointer < cnt_n:
                task = neutral[neutral_pointer]
                neutral_pointer += 1
            else:
                task = best_if_vasya_start[cnt_m - masha_pointer - 1]
                masha_pointer += 1
            res += tasks[task][1]
            day += len(task)
            n -= 1

    return res

for _ in range(1):
    n = randint(1,8)
    tasks = []
    for _ in range(n):
        cnt = randint(1, 50)
        letters = []
        for _ in range(cnt):
            letters.append(choice(['S', 'D']))
        tasks.append(''.join(letters))

    slow_res = slow(tasks)
    fast_res = fast(n, tasks)
    if slow_res != fast_res:
        print(tasks)
        print('slow:', slow_res)
        print('fast:', fast_res)

    print('all right')
    print(n)
    print(*tasks, sep='\n')
    print(slow_res)
