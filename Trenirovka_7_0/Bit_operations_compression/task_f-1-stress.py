# Вариант рабочий, но не проходит по времени при N около 1000, чуть быстрее предыдущего
import random
import time


def main(n, k, rows):
    snap_z = [[0] * (n + 1) for _ in range(n + 1)]
    x_z = [set(range(1, n + 1)) if i != 0 else set() for i in range(n + 1)]
    y_z = [set(range(1, n + 1)) if i != 0 else set() for i in range(n + 1)]

    for i in range(k):
        x, y, z = map(int, rows[i].split())
        if z in x_z[x]:
            x_z[x].remove(z)
        if z in y_z[y]:
            y_z[y].remove(z)
        snap_z[x][y] = 1

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if snap_z[x][y] == 0 and x_z[x] and y_z[y]:
                inter = x_z[x] & y_z[y]
                if inter:
                    return x, y, inter.pop()
    return -1


n, k = 1000, 1000000
data = []
for _ in range(k):
    x = str(random.randint(1, n))
    y = str(random.randint(1, n))
    z = str(random.randint(1, n))
    data.append(' '.join([x, y, z]))

start = time.time()
res = main(n, k, data)
if res == -1:
    print("YES")
else:
    print("NO")
    print(*res)
print(time.time() - start)
