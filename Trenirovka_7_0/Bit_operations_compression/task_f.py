# Вариант рабочий, но не проходит по времени при N около 1000
import sys

n, k = map(int, sys.stdin.readline().split())
cube = [[set(range(1, n + 1)), set(range(1, n + 1))] if i != 0 else [set(), set()] for i in range(n + 1)]
snap_z = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    x, y, z = map(int, sys.stdin.readline().split())
    if x in cube[z][0]:
        cube[z][0].remove(x)
    if y in cube[z][1]:
        cube[z][1].remove(y)
    snap_z[x][y] = 1

flag_no = False
for z in range(1, n + 1):
    if cube[z][0]:
        for xp in cube[z][0]:
            for yp in cube[z][1]:
                if snap_z[xp][yp] == 0:
                    flag_no = True
                    print('NO')
                    print(xp, yp, z)
                    break
            if flag_no:
                break
    if flag_no:
        break
else:
    print('YES')
