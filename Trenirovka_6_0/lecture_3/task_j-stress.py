import random
import time
from collections import deque


def slow(arr, h):
    min_dif = 1000000000
    right = 0
    temp = arr[-1][1] + arr[0][1]
    for left in range(n):
        temp -= arr[left - 1][1]
        while temp < h and right < (n - 1):
            right += 1
            temp += arr[right][1]
        if temp >= h:
            max_dif = 0
            for i in range(left, right):
                dif = arr[i + 1][0] - arr[i][0]
                max_dif = max(max_dif, dif)
            min_dif = min(min_dif, max_dif)
    return min_dif


def fast(chairs, H):
    dif = [0] * n
    for i in range(1, n):
        dif[i] = chairs[i][0] - chairs[i - 1][0]

    que = deque()
    temp = chairs[0][1]
    right = 0
    que.append((dif[0], 0))
    while temp < H and right < (n - 1):
        right += 1
        temp += chairs[right][1]
        while que and dif[right] > que[-1][0]:
            que.pop()
        que.append((dif[right], right))
    min_dif = que[0][0]
    for left in range(1, n):
        temp -= chairs[left - 1][1]
        if que[0][1] <= left:
            que.popleft()
        while temp < H and right < (n - 1):
            right += 1
            temp += chairs[right][1]
            if left == right:
                que = deque()
                que.append((0, left))
            else:
                while que and dif[right] > que[-1][0]:
                    que.pop()
                que.append((dif[right], right))
        if left == right:
            que = deque()
            que.append((0, left))
        if temp >= H:
            min_dif = min(min_dif, que[0][0])

    return min_dif


for _ in range(1000000):
    n = random.randint(1, 10)
    H = random.randint(1, 20)
    h = []
    w = []
    for _ in range(n):
        h.append(random.randint(1, 20))
        w.append(random.randint(1, 20))
    while sum(w) < H:
        w = [x + 1 for x in w]
    chairs = list(zip(h, w))
    chairs.sort()

    res1 = slow(chairs, H)
    res2 = fast(chairs, H)
    if res1 != res2:
        print(n, H)
        print(*h)
        print(*w)
        print(f'slow: {res1}, fast: {res2}')
        print()

# t1 = time.time()
# n = 200000
# H = 1000000
# h = []
# w = []
# for _ in range(n):
#     h.append(random.randint(1, 1000000000))
#     w.append(random.randint(10000, 1000000000))
# # while sum(w) < H:
# #     w = [x + 1 for x in w]
# chairs = list(zip(h, w))
# chairs.sort()
# fast(chairs, H)
# print(time.time() - t1)
