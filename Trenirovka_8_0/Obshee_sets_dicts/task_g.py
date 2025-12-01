def check_row(arr: list):
    tmp = 0
    if arr[0] != '.':
        tmp = 1
    for i in range(1, len(arr)):
        if tmp >= 5:
            return True
        if arr[i] != '.' and arr[i] == arr[i - 1]:
            tmp += 1
        elif arr[i] != '.':
            tmp = 1
        else:
            tmp = 0
    return tmp >= 5


def check_table(table, n, m):
    for j in range(m):
        col_res = check_row([table[i][j] for i in range(n)])
        if col_res:
            return True
    if n < 5 or m < 5:
        return False
    for a in range(n - 5, -(m -6), -1):
        diag_res = check_row([table[i][i - a] for i in range(n) if 0 <= i - a < m])
        if diag_res:
            return True
    for b in range(4, n + m - 5):
        diag_res = check_row([table[i][b - i] for i in range(n) if 0 <= b - i < m])
        if diag_res:
            return True
    return False


n, m = map(int, input().split())
table = []
res = False
for _ in range(n):
    row = list(input().strip())
    if check_row(row):
        res = True
    table.append(row)
if not res:
    res = check_table(table, n, m)

print(['No', 'Yes'][res])
