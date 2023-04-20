# На числовой прямой окрасили N отрезков. Известны координаты левого и правого концов каждого
# отрезка (Li и Ri). Найти длину окрашенной части числовой прямой.
# Формат ввода
# В первой строке находится число N, в следующих N строках - пары Li и Ri. Li и Ri - целые,
# -109 ≤ Li ≤ Ri ≤ 109, 1 ≤ N ≤ input-15.txt 000
# Формат вывода
# Вывести одно число - длину окрашенной части прямой.


n = int(input())
segms = []
for _ in range(n):
    p1, p2 = [int(x) for x in input().split()]
    segms.append((p1, -1))
    segms.append((p2, 1))
segms.sort()
nsegm = 0
long = 0
for i in range(n * 2):
    if nsegm > 0:
        long += segms[i][0] - segms[i - 1][0]
    nsegm -= segms[i][1]
print(long)
