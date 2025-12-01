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


n, k = map(int, input().split())
print(number_after_seconds(n, k))
