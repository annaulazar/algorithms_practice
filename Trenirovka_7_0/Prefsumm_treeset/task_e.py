def get_treeset(array):
    degree_two = 0
    while 2 ** degree_two < len(array):
        degree_two += 1
    size = 2 ** degree_two
    tree_set = [0] * (size * 2 - 1)  # кол-во нулей
    for i in range(len(array)):
        if array[i] == 0:
            tree_set[i + size - 1] = 1
        else:
            tree_set[i + size - 1] = 0
    for j in range(size - 2, -1, -1):
        left_child = tree_set[2 * j + 1]
        right_child = tree_set[2 * j + 2]
        tree_set[j] = left_child + right_child

    return tree_set, size


def get_cnt_zerros(l, r, tree, sec_l, sec_r, root=0):
    if l <= sec_l and r >= sec_r:
        return tree[root]
    elif r < sec_l or l > sec_r:
        return 0
    else:
        left_child_l = sec_l
        left_child_r = (sec_l + sec_r) // 2
        res_left = get_cnt_zerros(l, r, tree, left_child_l, left_child_r, root * 2 + 1)
        right_child_l = (sec_l + sec_r) // 2 + 1
        right_child_r = sec_r
        res_right = get_cnt_zerros(l, r, tree, right_child_l, right_child_r, root * 2 + 2)
        return res_left + res_right


def get_k_zerro_on_pref(r, k_, tree, sec_l, sec_r, root=0):
    if r < sec_l:
        return -1
    if sec_l == sec_r and tree[root] == 1 and k_ == 1:
        return root
    if sec_l == sec_r:
        return -1
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    cnt_zerros_left = tree[root * 2 + 1]
    right_child_l = (sec_l + sec_r) // 2 + 1
    right_child_r = sec_r
    cnt_zerros_right = tree[root * 2 + 2]
    if k_ <= cnt_zerros_left:
        return get_k_zerro_on_pref(r, k_, tree, left_child_l, left_child_r, root * 2 + 1)
    elif cnt_zerros_left < k_ <= cnt_zerros_left + cnt_zerros_right:
        return get_k_zerro_on_pref(r, k_ - cnt_zerros_left, tree, right_child_l, right_child_r, root * 2 + 2)
    else:
        return -1


def update_number(ind, new_value, tree):
    if new_value == 0:
        tree[ind] = 1
    else:
        tree[ind] = 0
    parent = (ind - 1) // 2
    while parent >= 0:
        left_child = tree[2 * parent + 1]
        right_child = tree[2 * parent + 2]
        tree[parent] = left_child + right_child
        parent = (parent - 1) // 2


n = int(input())
a = list(map(int, input().split()))
tree_cnt_zerros, n_ = get_treeset(a)
m = int(input())
res = []
for _ in range(m):
    row = input().split()
    command = row[0].strip()
    if command == 's':
        left, right, k = map(int, row[1:])
        cnt_zerros_pref = get_cnt_zerros(0, left - 2, tree_cnt_zerros, 0, n_ - 1)
        index = get_k_zerro_on_pref(right - 1, k + cnt_zerros_pref, tree_cnt_zerros, 0, n_ - 1)
        if index != -1:
            index = index - n_ + 2
        res.append(index)
    else:
        ind, value = map(int, row[1:])
        update_number(ind - 1 + n_ - 1, value, tree_cnt_zerros)

print(*res)
