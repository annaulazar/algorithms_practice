def print_table(table):
    for row in table:
        print(''.join(row))


n, m = map(int, input().split())
table = [[""] * m for _ in range(n)]
for i in range(n):
    row = input().strip()
    for j in range(m):
        table[i][j] = row[j]

flag_a = False
flag_b = False
t_a, b_a, l_a, r_a = -1, -1, -1, -1
t_b, b_b, l_b, r_b = -1, -1, -1, -1
count_wrong = 0
for i in range(n):
    for j in range(m):
        if table[i][j] == '#':
            if not flag_a:
                flag_a = True
                l_a = j
                t_a = i
                x = i
                while x < n:
                    y = j
                    while y < m:
                        if table[x][y] == '#':
                            if r_a == -1 or y <= r_a:
                                y += 1
                            elif r_a != -1 and y > r_a and (l_a - 1 < 0 or table[x][l_a - 1] == '.'):
                                break
                            else:
                                b_a = x - 1
                                break
                        else:
                            if r_a == -1:
                                r_a = y - 1
                                break
                            elif y - 1 < r_a:
                                b_a = x - 1
                                break
                            else:
                                break
                    else:
                        if r_a == -1:
                            r_a = m - 1
                    if b_a != -1:
                        break
                    x += 1
                if b_a == -1:
                    b_a = n - 1
                for p in range(t_a, b_a + 1):
                    for q in range(l_a, r_a + 1):
                        table[p][q] = 'a'

            elif flag_a and not flag_b:
                flag_b = True
                l_b = j
                t_b = i
                x = i
                while x < n:
                    y = j
                    while y < m:
                        if table[x][y] == '#':
                            if r_b == -1 or y <= r_b:
                                y += 1
                            elif r_b != -1 and y > r_b and (l_b - 1 < 0 or table[x][l_b - 1] == '.'):
                                break
                            else:
                                b_b = x - 1
                                break
                        else:
                            if r_b == -1:
                                r_b = y - 1
                                break
                            elif y - 1 < r_b:
                                b_b = x - 1
                                break
                            else:
                                break
                    else:
                        if r_b == -1:
                            r_b = m - 1
                    if b_b != -1:
                        break
                    x += 1
                if b_b == -1:
                    b_b = n - 1
                for p in range(t_b, b_b + 1):
                    for q in range(l_b, r_b + 1):
                        table[p][q] = 'b'

            elif flag_a and flag_b:
                count_wrong += 1


if not flag_b:
    if r_a - l_a == 0 and b_a - t_a == 0:
        print('NO')
    else:
        if r_a - l_a > 0:
            for k in range(t_a, b_a + 1):
                table[k][r_a] = 'b'
        else:
            table[b_a][l_a] = 'b'
        print('YES')
        print_table(table)
else:
    if count_wrong > 0:
        print('NO')
    else:
        print('YES')
        print_table(table)


