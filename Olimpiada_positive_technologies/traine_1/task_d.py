import math

n = int(input())
points = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    points.append((x, y, i))
points.sort(key=lambda k: k[0] ** 2 + k[1] ** 2)

dist_2 = math.ceil(((points[-1][0] - points[0][0]) ** 2 + (points[-1][1] - points[0][1]) ** 2) / 4)
res_ind = 0
for ind in range(n):
    temp_dist_2 = (points[ind][0] - points[0][0]) ** 2 + (points[ind][1] - points[0][1]) ** 2
    if temp_dist_2 > dist_2:
        res_ind = ind
        break
print(res_ind)
numbers = sorted([p[2] for p in points[:res_ind]])
print(*numbers)
