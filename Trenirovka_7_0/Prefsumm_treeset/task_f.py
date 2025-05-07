def get_treeset(array):
    degree_two = 0
    while 2 ** degree_two < len(array):
        degree_two += 1
    size = 2 ** degree_two
    tree_set = [-1] * (size * 2 - 1)  # максимум
    for i in range(len(array)):
        tree_set[i + size - 1] = array[i]
    for j in range(size - 2, -1, -1):
        left_child = tree_set[2 * j + 1]
        right_child = tree_set[2 * j + 2]
        tree_set[j] = max(left_child, right_child)

    return tree_set, size


def get_first_gte(l, value, tree, sec_l, sec_r, root=0):
    if sec_l == sec_r and value <= tree[root]:
        return root
    if value > tree[root]:
        return -1
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    max_left = tree[root * 2 + 1]
    right_child_l = (sec_l + sec_r) // 2 + 1
    right_child_r = sec_r
    res_left = -1
    if l <= left_child_r and value <= max_left:
        res_left = get_first_gte(l, value, tree, left_child_l, left_child_r, root * 2 + 1)
    if res_left == -1:
        return get_first_gte(l, value, tree, right_child_l, right_child_r, root * 2 + 2)
    return res_left


def update_number(ind, new_value, tree):
    tree[ind] = new_value
    parent = (ind - 1) // 2
    while parent >= 0:
        left_child = tree[2 * parent + 1]
        right_child = tree[2 * parent + 2]
        tree[parent] = max(left_child, right_child)
        parent = (parent - 1) // 2


n, m = map(int, input().split())
a = list(map(int, input().split()))
tree_max, n_ = get_treeset(a)
res = []
for _ in range(m):
    command, first, second = map(int, input().split())
    if command == 1:
        index = get_first_gte(first - 1, second, tree_max, 0, n_ - 1)
        if index != -1:
            index = index - n_ + 2
        res.append(index)
    else:
        update_number(first - 1 + n_ - 1, second, tree_max)

print(*res, sep='\n')
