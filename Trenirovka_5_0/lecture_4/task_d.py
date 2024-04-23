def get_long(width, words, max_word, cnt):
    if width < max_word:
        return -1
    long = 0
    index = 0
    while index < cnt:
        long += 1
        j = 0
        while index < cnt and j < width and width - j >= words[index]:
            j += words[index]
            index += 1
            j += 1
    return long


def lbinpoisk(l, r):
    while l < r:
        mid = (l + r) // 2
        res_left = get_long(mid, a, max_a, n)
        res_right = get_long(w - mid, b, max_b, m)
        if res_right == -1 or res_left <= res_right:
            r = mid
        else:
            l = mid + 1
    if get_long(w - l, b, max_b, m) == -1:
        return max(get_long(l - 1, a, max_a, n), get_long(w - l + 1, b, max_b, m))
    if get_long(l - 1, a, max_a, n) == -1:
        return max(get_long(l, a, max_a, n), get_long(w - l, b, max_b, m))
    res1 = max(get_long(l, a, max_a, n), get_long(w - l, b, max_b, m))
    res2 = max(get_long(l - 1, a, max_a, n), get_long(w - l + 1, b, max_b, m))
    return min(res1, res2)


w, n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
max_a = max(a)
max_b = max(b)
left = max_a
right = w
res = lbinpoisk(left, right)
print(res)
