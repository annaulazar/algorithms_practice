def update_tree(ind, add_value, tree):
    while ind < n:
        tree[ind] += add_value
        ind |= (ind + 1)


def sum_pref(ind, tree) -> int:
    res = 0
    while ind >= 0:
        res += tree[ind]
        ind = (ind & (ind + 1)) - 1
    return res


n, k = map(int, input().split())
a = [0] * n
fenv_tree = [0] * n
for _ in range(k):
    command, first, second = input().split()
    if command == 'A':
        index = int(first) - 1
        new_value = int(second)
        update_tree(index, new_value - a[index], fenv_tree)
        a[index] = new_value
    else:
        left = int(first) - 1
        right = int(second) - 1
        answer = sum_pref(right, fenv_tree) - sum_pref(left - 1, fenv_tree)
        print(answer)
