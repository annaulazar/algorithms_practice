# Функция генерации чисел длиной n в m-й cистеме счисления
def gen_number(n, m, s):
    if n == 0:
        print(s)
        return
    for i in range(m):
        gen_number(n - 1, m, s + str(i))


# Функция генерации перестановок чисел от 1 до n
def perm(n, used, p):
    if len(p) == n:
        print(*p)
        return
    for i in range(1, n + 1):
        if not used[i - 1]:
            used[i - 1] = True
            p.append(i)
            perm(n, used, p)
            used[i - 1] = False
            p.pop()


# функция генерации упорядоченных слагаемых числа
def gen_terms(n, last, p):
    if n == 0:
        print(*p)
        return
    for i in range(last, n // 2 + 1):
        p.append(i)
        gen_terms(n - i, i, p)
        p.pop()
    p.append(n)
    gen_terms(0, n, p)
    p.pop()


# Размещения из n по k - кол-во упорядоченных наборов длины k из n элементов без повторений (порядок важен)
def placements(n, k, used, p):
    if len(p) == k:
        print(*p)
        return
    for i in range(1, n + 1):
        if not used[i - 1]:
            used[i - 1] = True
            p.append(i)
            placements(n, k, used, p)
            used[i - 1] = False
            p.pop()


# Сочетания из n по k - кол-во неупорядоченных наборов длины k из n элементов без повторений (порядок не важен)
def combinations(n, k, last, p):
    if k == 0:
        print(*p)
        return
    l = last + 1
    r = n - k + 1
    for i in range(l, r + 1):
        p.append(i)
        combinations(n, k - 1, i, p)
        p.pop()


# gen_number(3, 2, '')
# perm(4, [False for _ in range(4)], [])
# gen_terms(7, 2, [])
# placements(4, 2, [False for _ in range(4)], [])
print("-------")
combinations(4, 2, 0, [])


