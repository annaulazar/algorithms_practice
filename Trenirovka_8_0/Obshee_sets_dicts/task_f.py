n, m = map(int, input().split())

rows = [0] * n
columns = [0] * m
table = [['-'] * m for _ in range(n)]
for i in range(n):
    row = input().strip()
    row_sum = 0
    for j in range(m):
        if row[j] == '+':
            row_sum += 1
            columns[j] += 1
        elif row[j] == '-':
            row_sum -= 1
            columns[j] -= 1
        else:
            row_sum += 1
            columns[j] -= 1
            table[i][j] = '?'
    rows[i] = row_sum

rows_sort = sorted([(v, ind) for ind, v in enumerate(rows)])
columns_sort = sorted([(v, ind) for ind, v in enumerate(columns)])

row_ind = n - 1
start_diff = rows_sort[-1][0] - columns_sort[0][0]
max_diff = start_diff
if table[rows_sort[-1][1]][columns_sort[0][1]] != '?':
    print(max_diff)
else:
    max_diff -= 2
    while row_ind >= 0 and rows_sort[-1][0] - rows_sort[row_ind][0] < 2:
        col_ind = 0
        while col_ind < m and start_diff - (rows_sort[row_ind][0] - columns_sort[col_ind][0]) < 2:
            temp_diff = rows_sort[row_ind][0] - columns_sort[col_ind][0]
            if table[rows_sort[row_ind][1]][columns_sort[col_ind][1]] == '?':
                temp_diff -= 2
            if temp_diff > max_diff:
                max_diff = temp_diff
            col_ind += 1
        row_ind -= 1
    print(max_diff)
