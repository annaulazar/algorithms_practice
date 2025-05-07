from collections import deque

table = [[-1] * 10 for _ in range(10)]
x1, y1 = map(int, input()[1:-1].split(', '))
x2, y2 = map(int, input()[1:-1].split(', '))
n = int(input())
for _ in range(n):
	x, y = map(int, input()[1:-1].split(', '))
	table[x][y] = -2
que = deque()
que.append((x1, y1))
table[x1][y1] = 0
deltas = ((0, -1), (-1, 0), (0, 1), (1, 0))
while que:
	xt, yt = que.popleft()
	for dx, dy in deltas:
		if 0 <= xt + dx <= 9 and 0 <= yt + dy <= 9 and table[xt + dx][yt + dy] == -1:
			table[xt + dx][yt + dy] = table[xt][yt] + 1
			que.append((xt + dx, yt + dy))
if table[x2][y2] == -1 or table[x2][y2] == -2:
	print('Добраться не получится')
else:
	print(table[x2][y2])
