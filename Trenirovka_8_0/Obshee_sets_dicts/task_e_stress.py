from random import randint

def number_after_seconds(n, k):
    last = int(str(n)[-1])
    first = n - last
    if k == 0 or last == 0:
        return n
    if last == 5:
        return n + 5
    if last in (1, 2, 4, 8):
        k += (1, 2, 4, 8).index(last)
        if k % 4 == 0:
            second = k // 4 * 20 - 4
        else:
            second = (k // 4) * 20 + 2 ** (k % 4)
    else:
        k += (3, 6, 7, 9).index(last)
        if (k - 1) % 4 == 0:
            second = ((k - 1) // 4) * 20 + 6
        else:
            second = 10 + ((k - 1) // 4) * 20 + 2 ** ((k - 1) % 4)
    return first + second


def slow_method(n, k):
    for i in range(k):
        n += int(str(n)[-1])
    return n

for _ in range(1000):
    n = randint(0, 100000)
    k = randint(0, 20000)
    slow = slow_method(n, k)
    fast = number_after_seconds(n, k)
    if slow != fast:
        print(n, k)
        print(f'slow: {slow}, fast: {fast}')
        print('-----------------------')

#
# n, k = map(int, input().split())
# print(slow_method(n, k))
