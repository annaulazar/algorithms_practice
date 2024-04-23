# Решение по разбору https://svgimnazia1.grodno.by/sinica/Book_ABC/Book_ABC_pascal/olimp_resh/olimp_resh55.htm
# с подсчетом трапеций и переливаниями с поглощениями вправо и влево. До конца не сделано, неправильно начала
# трапеции считать, надо трапеции присоединять, а я сумму считала.


row = input().strip().split()
n = int(row[0])
H = float(row[1])
x0, y0 = map(int, input().split())
points = [(x0, 10**9 + 10), (x0, y0)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    points.append((x, y))
points.append((points[-1][0], 10**9 + 10))

peaks = [(points[0][1], 0)] # Координаты у и номера вершин
lows = [] # Координаты у и номера низин
for i in range(1, n - 1):
    if points[i - 1][1] < points[i][1] > points[i + 1][1]:
        peaks.append((points[i][1], i))
    elif points[i - 1][1] > points[i][1] < points[i + 1][1]:
        lows.append((points[i][1], i))
peaks = [(points[-1][1], n -1)]
n_peaks = len(peaks)
n_lows = len(lows)

start_v = [] # Первоначальный объем воды по низинам, берем координаты х соседних вершин
for j in range(n_lows):
    v = (points[peaks[j + 1][1]][0] - points[peaks[j][1]][0]) * H
    start_v.append(v)

s_lows = [0] * n_lows # Объемы низин
for l in range(n_lows):
    ind_low = lows[l][1]
    x_low = points[ind_low][0]
    y_low = lows[l][0]
    y_max = min(peaks[l][0], peaks[l + 1][0]) # - минимальная вершина ближайшая

    s = 0
    # Идем влево до меньшей вершины или точки выше вершины
    ind = ind_low - 1
    w = 0
    flag_v = False
    while ind >= 0 and points[ind][1] <= y_max:
        s += ((x_low - points[ind][0]) + w) * (points[ind][1] - points[ind + 1][1]) / 2
        w = x_low - points[ind][0]
        if points[ind][1] == y_max:
            flag_v = True
        ind -= 1
    if not flag_v:
        delta = (points[ind + 1][0] - points[ind][0]) * (y_max - points[ind + 1][1]) / (points[ind][1] - points[ind + 1][1])
        s += (w + delta + w) * (y_max - points[ind + 1][1]) / 2

    # Идем вправо до меньшей вершины или точки выше вершины
    ind = ind_low + 1
    w = 0
    flag_v = False
    while ind <= n - 1 and points[ind][1] <= y_max:
        s += ((points[ind][0] - x_low) + w) * (points[ind][1] - points[ind - 1][1]) / 2
        w = points[ind][0] - x_low
        if points[ind][1] == y_max:
            flag_v = True
        ind += 1
    if not flag_v:
        delta = (points[ind][0] - points[ind - 1][0]) * (y_max - points[ind - 1][1]) / (
                    points[ind][1] - points[ind - 1][1])
        s += (w + delta + w) * (y_max - points[ind - 1][1]) / 2

    s_lows[l] = s

s_peaks = [0] * n_peaks # Объемы вершин
for p in range(1, n_peaks - 1):
    ind_peak = peaks[p][1]
    x_peak = points[ind_peak][0]
    y_peak = peaks[p][0]
    # Ищем ближайшую минимальную вершину которая выше
    y_max_peak = y_peak
    for left in range(p - 1, -1, -1):
        if peaks[left] > y_max_peak:
            y_max_peak = peaks[left]
            break
    for right in range(p + 1, n_peaks):
        if y_max_peak > peaks[right] > y_peak:
            y_max_peak = peaks[right]
            break
        elif peaks[right] > y_max_peak:
            break

    s = 0
    # Идем влево до меньшей вершины или точки выше вершины
    ind = ind_peak - 1
    w = 0
    y = y_peak
    flag_v = False
    while ind >= 0 and points[ind][1] <= y_max_peak:
        if points[ind][1] > y_peak:
            if w == 0:
                delta = (points[ind + 1][0] - points[ind][0]) * (points[ind][1] - y_peak) / (points[ind][1] - points[ind + 1][1])
                w = x_peak - points[ind][0] - delta
            s += ((x_peak - points[ind][0]) + w) * (points[ind][1] - y) / 2
            w = x_peak - points[ind][0]
            y = points[ind][1]
            if points[ind][1] == y_max_peak:
                flag_v = True
        ind -= 1
    if not flag_v:
        delta = (points[ind + 1][0] - points[ind][0]) * (y_max_peak - points[ind + 1][1]) / (
                    points[ind][1] - points[ind + 1][1])
        s += (w + delta + w) * (y_max_peak - y) / 2

    # Идем вправо до меньшей вершины или точки выше вершины
    ind = ind_peak + 1
    w = 0
    y = y_peak
    flag_v = False
    while ind <= n - 1 and points[ind][1] <= y_max_peak:
        if points[ind][1] > y_peak:
            if w == 0:
                delta = (points[ind][0] - points[ind - 1][0]) * (points[ind][1] - y_peak) / (
                            points[ind][1] - points[ind - 1][1])
                w = points[ind][0] - x_peak - delta
            s += ((points[ind][0] - x_peak) + w) * (points[ind][1] - y) / 2
            w = points[ind][0] - x_peak
            if points[ind][1] == y_max_peak:
                flag_v = True
        ind += 1
    if not flag_v:
        delta = (points[ind][0] - points[ind - 1][0]) * (y_max_peak - points[ind - 1][1]) / (
                points[ind][1] - points[ind - 1][1])
        s += (w + delta + w) * (y_max_peak - y) / 2

    s_peaks[p] = s

flag_over = True
while flag_over:
    overs = 0
    for q in range(len(lows) - 1, 0, -1):
        s_own = s_lows[q]
        if start_v[q] > s_own and peaks[q][0] < peaks[q + 1][0]:
            extra = start_v[q] - s_own
            start_v[q] -= extra
            start_v[q - 1] += extra
    for r in range(len(lows) - 1):
        s_own = s_lows[r]
        if s_own != 0:
            if start_v[r] > s_own and peaks[r + 1][0] < peaks[r][0]:
                extra = start_v[r] - s_own
                start_v[r] -= extra
                start_v[r + 1] += extra
                if peaks[r + 1][0] < peaks[r + 2][0]:
                    overs += 1
                    peaks[r + 1] = 0
                    if lows[r + 1][0] <  lows[r][0]:
                        start_v[r + 1] += start_v[r]
                        start_v[r] = 0
                        s_lows[r + 1] += s_lows[r] + s_peaks[r + 1]
                        s_lows[r] = 0
                        s_peaks[r + 1] = 0
                        lows[r] = 0
                    elif lows[r + 1][0] >  lows[r][0]:
                        start_v[r] += start_v[r + 1]
                        start_v[r + 1] = 0
                        s_lows[r] += s_lows[r + 1] + s_peaks[r + 1]
                        s_lows[r + 1] = 0
                        s_peaks[r + 1] = 0
                        lows[r + 1] = 0
    if overs == 0:
        flag_over = False
        break
    start_v = list(filter(None, start_v))
    s_lows = list(filter(None, s_lows))
    s_peaks = list(filter(None, s_peaks))
    peaks = list(filter(None, peaks))
    lows = list(filter(None, lows))


