def robot_left(x, y, letter: str, arr):
    while not(x == 1 and y == 1):
        if arr[x][y - 1] == '.':
            arr[x][y - 1] = letter
            y -= 1
        elif arr[x - 1][y] == '.':
            arr[x - 1][y] = letter
            x -= 1
    return arr


def robot_right(x, y, letter, arr, n, m):
    while not(x == n and y == m):
        if arr[x][y + 1] == '.':
            arr[x][y + 1] = letter
            y += 1
        elif arr[x + 1][y] == '.':
            arr[x + 1][y] = letter
            x += 1
    return arr


for _ in range(int(input())):
    n, m = map(int, input().split())
    table = [[0] * (m + 2) for _ in range(n + 2)]
    coords_a = (0, 0)
    coords_b = (0, 0)
    for i in range(n):
        row = input().strip()
        for j in range(m):
            symbol = row[j]
            table[i + 1][j + 1] = symbol
            if symbol == 'A':
                coords_a = (i + 1, j + 1)
            elif symbol == 'B':
                coords_b = (i + 1, j + 1)
    if coords_a[1] < coords_b[1] or coords_a[0] < coords_b[0]:
        table = robot_left(coords_a[0], coords_a[1], 'a', table)
        table = robot_right(coords_b[0], coords_b[1], 'b', table, n, m)
    else:
        table = robot_left(coords_b[0], coords_b[1], 'b', table)
        table = robot_right(coords_a[0], coords_a[1], 'a', table, n, m)


    for line in table[1: -1]:
        print(''.join(line[1:-1]))
