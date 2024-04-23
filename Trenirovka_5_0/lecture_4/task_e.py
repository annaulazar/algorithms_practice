import math

n = int(input())
k = math.ceil(((1 + 8 * n) ** 0.5 - 1) / 2) + 1
while True:
    last = (k + 1) * k // 2
    first = last - k + 1
    if first <= n <= last:
        break
    else:
        k -= 1
if k % 2 == 0:
    i = last - n + 1
else:
    i = n - first + 1
j = k - i + 1
print(f'{i}/{j}')
