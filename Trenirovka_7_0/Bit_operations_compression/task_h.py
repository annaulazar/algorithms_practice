import sys


def update_tree(x, y, z, add_value, tree, n):
    while x < n:
        y_cur = y
        while y_cur < n:
            z_cur = z
            while z_cur < n:
                tree[x][y_cur][z_cur] += add_value
                z_cur |= (z_cur + 1)
            y_cur |= (y_cur + 1)
        x |= (x + 1)


def sum_pref(x, y, z, tree) -> int:
    res = 0
    while x >= 0:
        y_cur = y
        while y_cur >= 0:
            z_cur = z
            while z_cur >= 0:
                res += tree[x][y_cur][z_cur]
                z_cur = (z_cur & (z_cur + 1)) - 1
            y_cur = (y_cur & (y_cur + 1)) - 1
        x = (x & (x + 1)) - 1
    return res


def sum_cube(x1, y1, z1, x2, y2, z2, tree):
    return (sum_pref(x2, y2, z2, tree) + sum_pref(x2, y1, z1, tree) +
            sum_pref(x1, y2, z1, tree) + sum_pref(x1, y1, z2, tree) -
            sum_pref(x1, y1, z1, tree) - sum_pref(x2, y2, z1, tree) -
            sum_pref(x2, y1, z2, tree) - sum_pref(x1, y2, z2, tree))


def main(n, commands):
    cub_fenv_tree = [[[0] * n for i in range(n)] for j in range(n)]
    answer = []
    for row in commands:
        if row.startswith('1'):
            x, y, z, k = map(int, row.split()[1:])
            update_tree(x, y, z, k, cub_fenv_tree, n)
        elif row.startswith('2'):
            x1, y1, z1, x2, y2, z2 = map(int, row.split()[1:])
            answer.append(sum_cube(x1 - 1, y1 - 1, z1 - 1, x2, y2, z2, cub_fenv_tree))
        else:
            return answer


n = int(sys.stdin.readline())
commands = sys.stdin
res = main(n, commands)
print(*res, sep='\n')
