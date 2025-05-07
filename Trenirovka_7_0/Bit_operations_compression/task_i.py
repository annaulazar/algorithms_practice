import math


def code(x):
    z = len(x)
    k = 1
    while math.log(z + k + 1, 2) > k:
        k += 1
    total = z + k
    arr = [0] * (total + 1)
    ind = 0
    step_2 = 0
    for i in range(1, total + 1):
        if 2 ** step_2 == i and step_2 < k:
            step_2 += 1
        else:
            arr[i] = int(x[ind])
            ind += 1
    for j in range(k):
        start = 2 ** j
        step = 2 ** (j + 1)
        cnt_ones = 0
        for p in range(start, total + 1, step):
            for q in range(p, p + start):
                if q <= total:
                    cnt_ones += arr[q]
        if cnt_ones % 2 == 0:
            arr[start] = 1

    return ''.join(map(str, arr[1:]))


def decode(y):
    total = len(y)
    k = math.ceil(math.log(total, 2))
    n_ = total - k
    arr = [0] + list(map(int, list(y)))
    wrong = 0
    for j in range(k):
        start = 2 ** j
        step = 2 ** (j + 1)
        cnt_ones = 0
        for p in range(start, total + 1, step):
            for q in range(p, p + start):
                if q <= total:
                    cnt_ones += arr[q]
        if cnt_ones % 2 == 0:
            wrong += 2 ** j
    if wrong != 0:
        arr[wrong] = abs(arr[wrong] - 1)
    res = []
    step_2 = 0
    for i in range(1, total + 1):
        if 2 ** step_2 == i and step_2 < k:
            step_2 += 1
        else:
            res.append(arr[i])

    return ''.join(map(str, res))


n = int(input())
s = input()
if n == 1:
    print(code(s))
else:
    print(decode(s))
