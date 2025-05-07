# Вариант рабочий, но не проходит по времени при N около 1000, чуть быстрее предыдущего
import time


start = time.time()

with open('input21.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    snap_z = [[0] * (n + 1) for _ in range(n + 1)]
    x_z = [set(range(1, n + 1)) if i != 0 else set() for i in range(n + 1)]  # небитые уровни z для каждого х
    y_z = [set(range(1, n + 1)) if i != 0 else set() for i in range(n + 1)]  # небитые уровни z для каждого y

    for row in file:
        x, y, z = map(int, row.split())
        if z in x_z[x]:
            x_z[x].remove(z)
        if z in y_z[y]:
            y_z[y].remove(z)
        snap_z[x][y] = 1

flag_no = False
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if snap_z[x][y] == 0 and x_z[x] and y_z[y]:
            inter = x_z[x] & y_z[y]
            if inter:
                flag_no = True
                print('NO')
                print(x, y, inter.pop())
                break
    if flag_no:
        break
else:
    print('YES')
print(time.time() - start)