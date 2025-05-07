import random


def slow(n, arr):
    res = float('inf')
    for i in range(n):
        trans = 0
        for j in range(n):
            trans += arr[j] * abs(j - i)
        res = min(res, trans)
    return res


def fast(n, a):
    pref_left = [0] * n
    pref_right = [0] * n
    pref_sum_left = [0] * n
    pref_sum_right = [0] * n
    for i in range(1, n):
        pref_left[i] = pref_left[i - 1] + a[i - 1]
        pref_sum_left[i] = pref_sum_left[i - 1] + pref_left[i]

    for j in range(n - 2, -1, -1):
        pref_right[j] = pref_right[j + 1] + a[j + 1]
        pref_sum_right[j] = pref_sum_right[j + 1] + pref_right[j]

    min_transitions = pref_sum_left[0] + pref_sum_right[0]
    for k in range(n):
        transitions = pref_sum_left[k] + pref_sum_right[k]
        min_transitions = min(min_transitions, transitions)

    return min_transitions

# n = int(input())
# a = list(map(int, input().split()))
#
# print(slow(n, a))
# print(fast(n, a))

for _ in range(1000000):
    n = random.randint(1, 10)
    a = []
    for _ in range(n):
        a.append(random.randint(1, 100))
    slow_res = slow(n, a)
    fast_res = fast(n, a)
    if slow_res != fast_res:
        print(n)
        print(*a)
        print(f'slow - {slow_res}, fast - {fast_res}')
