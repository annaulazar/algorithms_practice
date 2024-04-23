n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points_set = set(points)
flag3 = False
flag4 = False
res = []
for i in range(n - 1):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        deltax = x2 - x1
        deltay = y2 - y1
        cand1 = ((x1 + x2 + deltay) / 2, (y1 + y2 - deltax) / 2)
        cand2 = ((x1 + x2 - deltay) / 2, (y1 + y2 + deltax) / 2)
        if cand1 in points_set and cand2 in points_set:
            flag4 = True
            res = []
            break
        elif not flag3:
            if cand1 in points_set:
                res = [(int(cand2[0]), int(cand2[1]))]
                flag3 = True
            elif cand2 in points_set:
                res = [(int(cand1[0]), int(cand1[1]))]
                flag3 = True
    if flag4:
        break
if not flag3 and not flag4:
    x1, y1 = points[0]
    if n >= 2:
        x2, y2 = points[1]
        deltax = x2 - x1
        deltay = y2 - y1
        if abs(deltax) == abs(deltay):
            res.append((x1, y2))
            res.append((x2, y1))
        elif deltax == 0:
            res.append((x1 + deltay, y1))
            res.append((x2 + deltay, y2))
        elif deltay == 0:
            res.append((x1, y1 + deltax))
            res.append((x2, y2 + deltax))
        else:
            res.append((x1 + deltay, y1 - deltax))
            res.append((x2 + deltay, y2 - deltax))
    else:
        res.append((x1, y1 + 1))
        res.append((x1 + 1, y1))
        res.append((x1 + 1, y1 + 1))
print(len(res))
for point in res:
    print(*point)
