# Получение одной точки касания двух окружностей
def get_intersection(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    k = r0 / (r0 + r1)
    x2 = x0 + (x1 - x0) * k
    y2 = y0 + (y1 - y0) * k
    return x2, y2


# Получение двух точек переечения окружностей
def get_intersections(x0, y0, r0, x1, y1, r1, d):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    # d - distance between centers
    a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
    h = (r0 ** 2 - a ** 2) ** 0.5
    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d
    x3 = x2 + h * (y1 - y0) / d
    y3 = y2 - h * (x1 - x0) / d

    x4 = x2 - h * (y1 - y0) / d
    y4 = y2 + h * (x1 - x0) / d
    return x3, y3, x4, y4


# Функция проверяет что в момент времени t все точки полукруга достижимы, по определенным точкам,
# что каждая точка попадает хотя бы в одну окружность игрока
# Радиус окружности игрока - скорость * время
def check_time(t):
    points = [(-D, 0), (D, 0), (0, D), (0, 0)] # Сначала проверяем базовые точки по краям полукруга и в центре
    for x, y in points:
        for xp, yp, v in players:
            R = v * t
            d2 = (xp - x) ** 2 + (yp - y) ** 2
            if d2 <= R ** 2:
                break
        else:
            return False, x, y
    for i in range(n):
        x1, y1, v1 = players[i]
        R1 = v1 * t
        first_points = [] # Для каждого игрока проверяем точки около точек пересечения (касания) его окружности с линией у=0
        if y1 == R1 and -D < x1 < D:
            first_points.append((x1 - 0.0001, 0))
            first_points.append((x1 + 0.0001, 0))
        elif y1 < R1:
            d = (R1 ** 2 - y1 ** 2) ** 0.5
            first1x = x1 - d
            if -D  < first1x < D:
                first_points.append((first1x - 0.0001, 0))
            first2x = x1 + d
            if -D < first2x < D:
                first_points.append((first2x + 0.0001, 0))
        for x, y in first_points:
            for xp, yp, v in players:
                R = v * t
                d2 = (xp - x) ** 2 + (yp - y) ** 2
                if d2 <= R ** 2:
                    break
            else:
                return False, x, y

        for j in range(i + 1, n):
            temp_points = [] # Для каждой пары игроков находим точки пересечения или касания их окружностей и проверяем точки около них на маленьком расстоянии
            x2, y2, v2 = players[j]
            R2 = v2 * t
            dist2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
            dist = dist2 ** 0.5
            if (R1 + R2) ** 2 > dist2 > (abs(R1 - R2))**2:
                p1x, p1y, p2x, p2y = get_intersections(x1, y1, R1, x2, y2, R2, dist)
                deltax = p2x - p1x
                deltay = p2y - p1y
                kx = deltax / abs(deltay) if deltay != 0 else deltax / abs(deltax)
                ky = deltay / abs(deltax) if deltax != 0 else deltay / abs(deltay)
                cand1x, cand1y = p1x - kx * 0.0001, p1y - ky * 0.0001
                cand2x, cand2y = p2x + kx * 0.0001, p2y + ky * 0.0001
                if cand1y >= 0 and cand1x ** 2 + cand1y ** 2 <= D ** 2:
                    temp_points.append((cand1x, cand1y))
                if cand2y >= 0 and cand2x ** 2 + cand2y ** 2 <= D ** 2:
                    temp_points.append((cand2x, cand2y))
            elif dist2 == (R1 + R2) ** 2 or dist2 == (abs(R1 - R2))**2:
                p1x, p1y = get_intersection(x1, y1, R1, x2, y2, R2)
                deltax = x2 - x1
                deltay = y2 - y1
                kx = deltay / deltax if deltax != 0 else 1
                ky = deltax / deltay if deltay != 0 else 1
                cand1x, cand1y = p1x - kx * 0.0001, p1y + ky * 0.0001
                cand2x, cand2y = p1x + kx * 0.0001, p1y - ky * 0.0001
                if cand1y >= 0 and cand1x ** 2 + cand1y ** 2 <= D ** 2:
                    temp_points.append((cand1x, cand1y))
                if cand2y >= 0 and cand2x ** 2 + cand2y ** 2 <= D ** 2:
                    temp_points.append((cand2x, cand2y))
            for x, y in temp_points:
                for xp, yp, v in players:
                    R = v * t
                    d2 = (xp - x)**2 + (yp - y)**2
                    if d2 <= R**2:
                        break
                else:
                    return False, x, y
    return True, -1, -1


def lbinpoisk(l, r):
    while abs(l - r) > 0.0001:
        m = (l + r) / 2
        if check_time(m)[0]:
            r = m
        else:
            l = m + 0.0001
    return l


D, n = map(int, input().split())
players = []
for _ in range(n):
    x_, y_, v_ = map(int, input().split())
    players.append((x_, y_, v_))
time = lbinpoisk(0, 2000)
res_point = check_time(time - 0.0001)[1:]
res_x = float(res_point[0])
res_y = float(res_point[1])
print(time)
print(res_x, res_y)
