def chek_count(m, cnt):
    res = m * (m + 1) ** 2 // 2 - m * (m + 1) * (2 * m + 1) // 6 + m * (m + 1) // 2 - 1
    return res <= cnt


def rbinpoisk(l, r, cnt):
    while l < r:
        m = (l + r + 1) // 2
        if chek_count(m, cnt):
            l = m
        else:
            r = m - 1
    return r

n = int(input())
left = 1
right = n
k = rbinpoisk(left, right, n)
print(k)
