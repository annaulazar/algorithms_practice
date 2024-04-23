n = int(input())
matchesA = []
matchesB = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    matchesA.append((x1, y1, x2, y2))
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    matchesB.append((x1, y1, x2, y2))
deltas = {}
for matchB in matchesB:
    x_B1, y_B1, x_B2, y_B2 = matchB
    if x_B1 > x_B2:
        x_B1, x_B2 = x_B2, x_B1
        y_B1, y_B2 = y_B2, y_B1
    elif x_B1 == x_B2 and y_B1 > y_B2:
        y_B1, y_B2 = y_B2, y_B1
    for matchA in matchesA:
        x_A1, y_A1, x_A2, y_A2 = matchA
        if x_A1 > x_A2:
            x_A1, x_A2 = x_A2, x_A1
            y_A1, y_A2 = y_A2, y_A1
        elif x_A1 == x_A2 and y_A1 > y_A2:
            y_A1, y_A2 = y_A2, y_A1
        deltax1 = x_B1 - x_A1
        deltax2 = x_B2 - x_A2
        deltay1 = y_B1 - y_A1
        deltay2 = y_B2 - y_A2
        if deltax1 == deltax2 and deltay1 == deltay2:
            delta = (deltax1, deltay1)
            if delta not in deltas:
                deltas[delta] = 0
            deltas[delta] += 1

max_par = 0
for _, value in deltas.items():
    if value > max_par:
        max_par = value
print(n - max_par)

