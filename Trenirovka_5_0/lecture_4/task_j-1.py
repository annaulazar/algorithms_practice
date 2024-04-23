import sys

sys.setrecursionlimit(1500)


def check_volume(level, V, points, s_points, y_min):
    volume = (points[-1][0] - points[0][0]) * (level - y_min) - sum(s_points)
    if points[1][1] > level and points[1][0] != points[2][0]:
        delta = ((points[2][0] - points[1][0]) / (points[1][1] - points[2][1])) * (points[1][1] - level) ** 2 / 2
        volume += delta
    if points[-2][1] > level and points[-2][0] != points[-3][0]:
        delta = ((points[-2][0] - points[-3][0]) / (points[-2][1] - points[-3][1])) * (points[-2][1] - level) ** 2 / 2
        volume += delta
    return volume >= V


def lbinpoisk(l, r, V, points, s_points, y_min):
    while abs(l - r) > 0.001:
        m = (l + r) / 2
        if check_volume(m, V, points, s_points, y_min):
            r = m
        else:
            l = m + 0.001
    return l


def pool(points, V, max_deep=0):
    peaks = []  # Координаты у и номера вершин
    lows = []  # Координаты у и номера низин
    y_min = y_max
    for i in range(1, len(points) - 1):
        if points[i - 1][1] < points[i][1] > points[i + 1][1]:
            peaks.append((points[i][1], i))
        elif points[i - 1][1] > points[i][1] < points[i + 1][1]:
            lows.append((points[i][1], i))
            y_min = min(y_min, points[i][1])
    s_points = [0] * len(points)
    for i in range(1, len(points)):
        s_points[i] = ((points[i][1] - y_min) + (points[i - 1][1] - y_min)) * (points[i][0] - points[i - 1][0]) / 2
    level = lbinpoisk(y_min, y_max, V, points, s_points, y_min)
    max_peak = 0
    index = -1
    for j in range(len(peaks)):
        if peaks[j][0] > level and peaks[j][0] > max_peak:
            max_peak = peaks[j][0]
            index = peaks[j][1]
    if index == -1:
        return max(max_deep, level - y_min)
    V1 = (points[index][0] - points[0][0]) / (points[-1][0] - points[0][0]) * V
    V2 = V - V1
    points1 = points[:index + 1] + [(points[index][0], y_max)]
    points2 = [(points[index][0], y_max)] + points[index:]
    max_deep = max(max_deep, pool(points1, V1, max_deep))
    max_deep = max(max_deep, pool(points2, V2, max_deep))
    return  max_deep


row = input().strip().split()
n = int(row[0])
H = float(row[1])
x0, y0 = map(int, input().split())
y_max = y0
points = [(x0, 0), (x0, y0)]
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    y_max = max(y_max, y)
y_max = y_max + H + 10
points[0] = (x0, y_max)
points.append((points[-1][0], y_max))

V = (points[-1][0] - x0) * H

result = pool(points, V)
print(result)
