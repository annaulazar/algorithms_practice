# Красивая строка
# Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)
# Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа.
# Формат ввода
# В первой строке записано одно целое число k (0 ≤ k ≤ 109)
# Во второй строке дана непустая строчка S (|S| ≤ 2 ⋅ 105). Строчка S состоит только из маленьких латинских букв.
# Формат вывода
# Выведите одно число — максимально возможную красоту строчки, которую можно получить.

k = int(input())
s = input()
n = len(s)
letters = set(s)
if k >= n:
    print(n)
else:
    maxbeawty = 0
    for letter in letters:
        maxcnt = 0
        cnt = 0
        last = 0
        zamen = k
        for first in range(n):
            while last < n and (zamen > 0 or s[last] == letter):
                if s[last] != letter:
                    zamen -=1
                cnt += 1
                last += 1
            maxcnt = max(maxcnt, cnt)
            if s[first] != letter:
                zamen += 1
            cnt -= 1
        maxbeawty = max(maxbeawty, maxcnt)
    print(maxbeawty)




