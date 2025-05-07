def get_treeset(array):
    degree_two = 0
    while 2 ** degree_two < len(array):
        degree_two += 1
    size = 2 ** degree_two
    tree_set = [[-1, 0]] * (size * 2 - 1)  # [максимум, обещание]
    for i in range(len(array)):
        tree_set[i + size - 1] = [array[i], 0]
    for j in range(size - 2, -1, -1):
        left_child = tree_set[2 * j + 1][0]
        right_child = tree_set[2 * j + 2][0]
        tree_set[j] = [max(left_child, right_child), 0]

    return tree_set, size


def get_max(l, r, tree, sec_l, sec_r, root=0):
    if tree[root][1]:
        promise = tree[root][1]
        tree[root][1] = 0
        if sec_l != sec_r:
            tree[root * 2 + 1][0] += promise
            tree[root * 2 + 1][1] += promise
            tree[root * 2 + 2][0] += promise
            tree[root * 2 + 2][1] += promise
    if l <= sec_l and r >= sec_r:
        return tree[root][0]
    if r < sec_l or l > sec_r:
        return -1
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    res_left = get_max(l, r, tree, left_child_l, left_child_r, root * 2 + 1)
    right_child_l = (sec_l + sec_r) // 2 + 1
    right_child_r = sec_r
    res_right = get_max(l, r, tree, right_child_l, right_child_r, root * 2 + 2)
    return max(res_left, res_right)


def update_numbers(l, r, add_value, tree, sec_l, sec_r, root=0):
    if tree[root][1]:
        promise = tree[root][1]
        tree[root][1] = 0
        if sec_l != sec_r:
            tree[root * 2 + 1][0] += promise
            tree[root * 2 + 1][1] += promise
            tree[root * 2 + 2][0] += promise
            tree[root * 2 + 2][1] += promise
    if l <= sec_l and r >= sec_r:
        tree[root][0] += add_value
        tree[root][1] += add_value
        return tree[root][0]
    if r < sec_l or l > sec_r:
        return tree[root][0]
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    res_left = update_numbers(l, r, add_value, tree, left_child_l, left_child_r, root * 2 + 1)
    right_child_l = (sec_l + sec_r) // 2 + 1
    right_child_r = sec_r
    res_right = update_numbers(l, r, add_value, tree, right_child_l, right_child_r, root * 2 + 2)
    tree[root][0] = max(res_left, res_right)
    return max(res_left, res_right)


n = int(input())
a = list(map(int, input().split()))
tree_max, n_ = get_treeset(a)
m = int(input())
res = []
for _ in range(m):
    row = input().split()
    command = row[0].strip()
    if command == 'm':
        left, right = map(int, row[1:])
        res.append(get_max(left - 1, right - 1, tree_max, 0, n_ - 1))
    else:
        left, right, value = map(int, row[1:])
        update_numbers(left - 1, right - 1, value, tree_max, 0, n_ - 1)

print(*res)
