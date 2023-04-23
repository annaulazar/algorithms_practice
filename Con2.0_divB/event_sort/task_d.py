# На прямой в точках a1,a2,…,an (возможно, совпадающих) сидят n котят. На той же прямой лежат
# m отрезков [l1,r1],[l2,r2],…,[lm,rm]. Нужно для каждого отрезка узнать его наполненность котятами
# — сколько котят сидит на отрезке.
# Формат ввода
# На первой строке n и m (1≤n,m≤105). На второй строке n целых чисел ai (0≤ai≤109). Следующие
# m строк содержат пары целых чисел li,ri (0≤li≤ri≤109).
# Формат вывода
# Выведите m целых чисел. i-е число — наполненность котятами i-го отрезка.

# В худшем случае решение за n2, не проходит
# n, m = map(int, input().split())
# cats = [int(x) for x in input().split()]
# segms = []
# for i in range(m):
#     l, r = map(int, input().split())
#     segms.append((l, -1, i))
#     segms.append((r, 1, i))
# for cat in cats:
#     segms.append((cat, 0, 0))
# segms.sort()
# open = set()
# ans = [0] * m
# for segm in segms:
#     if segm[1] == -1:
#         open.add(segm[2])
#     elif segm[1] == 1:
#         open.remove(segm[2])
#     elif segm[1] == 0:
#         for seg in open:
#             ans[seg] += 1
# print(*ans)

n, m = map(int, input().split())
cats = [int(x) for x in input().split()]
segms = []
for i in range(m):
    l, r = map(int, input().split())
    segms.append((l, -1, i))
    segms.append((r, 1, i))
for cat in cats:
    segms.append((cat, 0, 0))
segms.sort()
ncats = 0
startcats = [0] * m
ans = [0] * m
for segm in segms:
    if segm[1] == -1:
        startcats[segm[2]] = ncats
    elif segm[1] == 1:
        ans[segm[2]] = ncats - startcats[segm[2]]
    elif segm[1] == 0:
        ncats += 1
print(*ans)


