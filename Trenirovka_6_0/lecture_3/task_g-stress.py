import random
import time
from collections import deque


def primitive_func(minutes: int, cnt_by_minute: int, arr: list[int]) -> int:
    res = 0
    que = deque()
    for minute in range(minutes):
        cnt = cnt_by_minute
        while que and cnt > 0:
            res += minute - que.popleft() + 1
            cnt -= 1
        current = arr[minute]
        if current > cnt:
            current -= cnt
            res += cnt
            while current:
                que.append(minute)
                current -= 1
        else:
            res += current
    for ost in que:
        res += minutes - ost + 1
    return res


def sum_time_in_pvz(minutes: int, cnt_by_minute: int, arr: list[int]) -> int:
    res = 0
    que = deque()
    for minute in range(minutes):
        cnt = cnt_by_minute
        while que and cnt > 0:
            if que[0][0] <= cnt:
                from_que = que.popleft()
                cnt -= from_que[0]
                res += from_que[0] * (minute - from_que[1] + 1)
            else:
                que[0][0] -= cnt
                res += cnt * (minute - que[0][1] + 1)
                cnt = 0
        current = arr[minute]
        if current > cnt:
            current -= cnt
            res += cnt
            que.append([current, minute])
        else:
            res += current
    for ost in que:
        res += ost[0] * (minutes - ost[1] + 1)

    return res


# n, b = map(int, input().split())
# a = list(map(int, input().split()))

# стресс-тест на максимальное кол-во
# t1 = time.time()
# n = 100000
# b = 10000000
# a = [100000000] * n

# рандомные тесты на сравнение
for _ in range(1000000):
    n = random.randint(1, 5)
    b = random.randint(1, 10)
    a = []
    for _ in range(n):
        a.append(random.randint(0, 10))
    answer1 = primitive_func(n, b, a)
    answer2 = sum_time_in_pvz(n, b, a)
    if answer1 != answer2:
        print(n, b)
        print(*a)
        print(f'primitive: {answer1}, base: {answer2}')
