import random
from time import time


def slow(n, arr_a, m, k, arr_x):
    answer = []
    for x in arr_x:
        pos = x - 1
        temp = 0
        while temp <= k and pos > 0:
            if arr_a[pos] > arr_a[pos - 1]:
                pos -= 1
            elif arr_a[pos] == arr_a[pos - 1] and temp < k:
                temp += 1
                pos -= 1
            else:
                break
        answer.append(pos + 1)
    return answer


def fast(n, a, m, k, x):
    pref_cnt = [0] * n
    left = 0
    temp = 0
    for right in range(1, n):
        if a[right] > a[right - 1]:
            pref_cnt[right] = right - left
        elif a[right] < a[right - 1]:
            temp = 0
            left = right
        elif a[right] == a[right - 1]:
            temp += 1
            while temp > k:
                left += 1
                if a[left] == a[left - 1]:
                    temp -= 1
            pref_cnt[right] = right - left
    answer = [0] * m
    for i in range(m):
        xi = x[i]
        stop_pos = xi - pref_cnt[xi - 1]
        answer[i] = stop_pos
    return answer

# n = int(input())
# a = list(map(int, input().split()))
# m, k = map(int, input().split())
# x = list(map(int, input().split()))

for _ in range(1000000):
    n = random.randint(1, 10)
    a = [random.randint(1, 100) for _ in range(n)]
    m = random.randint(1, n)
    k = random.randint(0, n)
    x = [random.randint(1, n) for _ in range(m)]
    res_slow = slow(n, a, m, k, x)
    res_fast = fast(n, a, m, k, x)
    if res_slow != res_fast:
        print(n)
        print(*a)
        print(m, k)
        print(*x)
        print('slow: ', res_slow)
        print('fast: ', res_fast)
        print()

# t1 = time()
# n = 400000
# a = list(range(1000000000, 1000000000 - n, -1))
# m = 400000
# k = 400000
# x = list(range(1, 400001))
# res = fast(n, a, m, k, x)
# print(time() - t1)
