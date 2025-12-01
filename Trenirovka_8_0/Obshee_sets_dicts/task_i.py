x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x = abs(x1 - x2)
y = abs(y1 - y2)
if x == 0 and y == 0:
    res = 0
elif x == 0 or y == 0:
    res = (x + y - 1) * 3
else:
    res = (x + y - 2) * 3 + 1

print(res)
