def get_treeset(array):
    degree_two = 0
    while 2 ** degree_two < len(array):
        degree_two += 1
    size = 2 ** degree_two
    tree_set = [(0, 0, 0, 1)] * (size * 2 - 1)  # (самый длинный отр. из 0 внутри, самый длинный префикс из 0, самый длинный суф. из 0, длина отрезка)
    for i in range(len(array)):
        if array[i] == 0:
            tree_set[i + size - 1] = (1, 1, 1, 1)
        else:
            tree_set[i + size - 1] = (0, 0, 0, 1)
    for j in range(size - 2, -1, -1):
        left_child = tree_set[2 * j + 1]
        right_child = tree_set[2 * j + 2]
        max_set = max(left_child[0], right_child[0], left_child[2] + right_child[1])
        if left_child[0] == left_child[3]:
            pref = left_child[0] + right_child[1]
        else:
            pref = left_child[1]
        if right_child[0] == right_child[3]:
            suf = right_child[0] + left_child[2]
        else:
            suf = right_child[2]
        length = left_child[3] + right_child[3]
        tree_set[j] = (max_set, pref, suf, length)

    return tree_set, size


def get_max_zerros_set(l, r, tree, sec_l, sec_r, root=0):
    if l <= sec_l and r >= sec_r:
        return tree[root]
    if r < sec_l or l > sec_r:
        return 0, 0, 0, tree[root][3]
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    res_left = get_max_zerros_set(l, r, tree, left_child_l, left_child_r, root * 2 + 1)
    right_child_l = (sec_l + sec_r) // 2 + 1
    right_child_r = sec_r
    res_right = get_max_zerros_set(l, r, tree, right_child_l, right_child_r, root * 2 + 2)
    max_set = max(res_left[0], res_right[0], res_left[2] + res_right[1])
    if res_left[0] == res_left[3]:
        pref = res_left[0] + res_right[1]
    else:
        pref = res_left[1]
    if res_right[0] == res_right[3]:
        suf = res_right[0] + res_left[2]
    else:
        suf = res_right[2]
    length = tree[root][3]
    return max_set, pref, suf, length


def update_number(ind, new_value, tree):
    if (new_value == 0 and tree[ind][0] == 1) or (new_value != 0 and tree[ind][0] == 0):
        return
    if new_value == 0:
        tree[ind] = (1, 1, 1, 1)
    else:
        tree[ind] = (0, 0, 0, 1)
    parent = (ind - 1) // 2
    while parent >= 0:
        left_child = tree[2 * parent + 1]
        right_child = tree[2 * parent + 2]
        max_set = max(left_child[0], right_child[0], left_child[2] + right_child[1])
        if left_child[0] == left_child[3]:
            pref = left_child[0] + right_child[1]
        else:
            pref = left_child[1]
        if right_child[0] == right_child[3]:
            suf = right_child[0] + left_child[2]
        else:
            suf = right_child[2]
        length = left_child[3] + right_child[3]
        tree[parent] = (max_set, pref, suf, length)
        parent = (parent - 1) // 2


n = int(input())
a = list(map(int, input().split()))
tree_cnt_zerros, n_ = get_treeset(a)
m = int(input())
res = []
for _ in range(m):
    row = input().split()
    command = row[0].strip()
    if command == 'QUERY':
        left, right = map(int, row[1:])
        answer = get_max_zerros_set(left - 1, right - 1, tree_cnt_zerros, 0, n_ - 1)
        res.append(answer[0])
    else:
        index, value = map(int, row[1:])
        update_number(index - 1 + n_ - 1, value, tree_cnt_zerros)

print(*res, sep='\n')
