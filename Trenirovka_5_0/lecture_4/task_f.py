from collections import deque
import sys


def binpoisk_find_index(l, r, num):
    while l < r:
        m = (l + r) // 2
        if keys[m] >= num:
            r = m
        else:
            l = m + 1
    return l


def check_tracks(k):
    deq_max = deque()
    deq_min = deque()
    x_start = keys[0]
    index = binpoisk_find_index(0, n_keys - 1, x_start + k)
    deq_max.append(tiles[index][-1])
    deq_min.append(tiles[index][0])
    for i in range(index + 1, n_keys):
        temp_max = tiles[i][-1]
        temp_min = tiles[i][0]
        while deq_min and temp_min < deq_min[-1]:
            deq_min.pop()
        while deq_max and temp_max > deq_max[-1]:
            deq_max.pop()
        deq_min.append(temp_min)
        deq_max.append(temp_max)
    y_max = deq_max[0]
    y_min = deq_min[0]
    if y_max - y_min + 1 <= k:
        return True
    for i in range(1, n_keys):
        x_start = keys[i]
        temp_max = tiles[i - 1][-1]
        temp_min = tiles[i - 1][0]
        while deq_min and temp_min < deq_min[-1]:
            deq_min.pop()
        while deq_max and temp_max > deq_max[-1]:
            deq_max.pop()
        deq_min.append(temp_min)
        deq_max.append(temp_max)
        while index < n_keys and keys[index] < x_start + k:
            temp_pop_min = tiles[index][0]
            temp_pop_max = tiles[index][-1]
            if temp_pop_min == deq_min[0]:
                deq_min.popleft()
            if temp_pop_max == deq_max[0]:
                deq_max.popleft()
            index += 1
        y_max = deq_max[0]
        y_min = deq_min[0]
        if y_max - y_min + 1 <= k:
            return True
    return False


def lbinpoisk(l, r):
    while l < r:
        m = (l + r) // 2
        if check_tracks(m):
            r = m
        else:
            l = m + 1
    return l


w, h, n = map(int, sys.stdin.readline().strip().split())
tiles_d = {}
for j in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    if x not in tiles_d:
        tiles_d[x] = []
    tiles_d[x].append(y)

keys = sorted(tiles_d.keys())
tiles = []
for key in keys:
    tiles.append((min(tiles_d[key]), max(tiles_d[key])))
n_keys = len(keys)
k_min = 1
k_max = min(w, h)
res = lbinpoisk(k_min, k_max)
print(res)
