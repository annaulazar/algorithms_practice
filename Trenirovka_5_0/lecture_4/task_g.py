def count_plus(k, cnt):
    cnt_plus = k * k * 5
    for x in range(long, 3 * k - 1, -1):
        if regions_pref[x][-1] < cnt_plus:
            return False
        for y in range(width, 3 * k - 1, -1):
            if regions_pref[x][y] < cnt_plus:
                break
            x1_1, y1_1, x2_1, y2_1 = x - 3 * k + 1, y - 2 * k + 1, x, y - k
            rect1 = (regions_pref[x2_1][y2_1] - regions_pref[x2_1][y1_1 - 1]
                    - regions_pref[x1_1 - 1][y2_1] + regions_pref[x1_1 - 1][y1_1 - 1])
            if rect1 != cnt:
                continue
            x1_2, y1_2, x2_2, y2_2 = x - 2 * k + 1, y - 3 * k + 1, x - k, y
            rect2 = (regions_pref[x2_2][y2_2] - regions_pref[x2_2][y1_2 - 1]
                     - regions_pref[x1_2 - 1][y2_2] + regions_pref[x1_2 - 1][y1_2 - 1])
            if rect2 != cnt:
                continue
            return True
    return False


def rbinpoisk(l, r):
    while l < r:
        m = (l + r + 1) // 2
        need = m * m * 3
        if count_plus(m, need):
            l = m
        else:
            r = m - 1
    return r


with open('input33.txt', 'r') as file:
    long, width = map(int, file.readline().strip().split())
    rows = file.readlines()

regions = [[0] * width for _ in range(long)]
regions_pref = [[0] * (width + 1) for _ in range(long + 1)]

for i in range(1, long + 1):
    row = rows[i - 1]
    for j in range(1, width + 1):
        if row[j - 1] == '#':
            regions[i - 1][j - 1] = 1
        regions_pref[i][j] = (regions_pref[i][j - 1] + regions_pref[i - 1][j] -
                              regions_pref[i - 1][j - 1] + regions[i - 1][j - 1])

k_min = 1
k_max = min(long, width) // 3
result = rbinpoisk(k_min, k_max)
print(result)
