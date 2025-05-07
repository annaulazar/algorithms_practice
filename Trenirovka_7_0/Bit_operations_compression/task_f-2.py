# Отрабатывает быстро, используется подобие bit_set, но не разбивается массив на чанки, а хранится полностью число, так как N до 1000
import sys

n, k = map(int, sys.stdin.readline().split())
snap_z = [[0] * n for _ in range(n)]
# небитые уровни z для каждого х и у, храним в виде одного числа, соответсвующего в двоичном виде на соответсвующем месте 0 или 1 (0 - небитые)
x_z = [0] * n
y_z = [0] * n

for _ in range(k):
    x, y, z = map(int, sys.stdin.readline().split())
    x = x - 1
    y = y - 1
    z = z - 1
    snap_z[x][y] = 1
    x_z[x] |= 1 << z
    y_z[y] |= 1 << z

template = int('1' * n, 2)
flag_no = False
for x in range(n):
    for y in range(n):
        if snap_z[x][y] == 0:
            inter = x_z[x] | y_z[y]
            if inter != template:
                inter_bin = bin(inter)[2:].zfill(n)
                for i in range(n):
                    if inter_bin[i] == '0':
                        flag_no = True
                        print('NO')
                        print(x + 1, y + 1, n - i)
                        break
        if flag_no:
            break
    if flag_no:
        break
else:
    print('YES')
