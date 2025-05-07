def get_treeset(array):
    degree_two = 0
    while 2 ** degree_two < len(array):
        degree_two += 1
    size = 2 ** degree_two
    tree_set = [0] * (size * 2 - 1)  # число или обещание
    for i in range(len(array)):
        tree_set[i + size - 1] = array[i]
    for j in range(size - 2, -1, -1):
        tree_set[j] = 0

    return tree_set, size


def get_num(ind, tree, sec_l, sec_r, root=0):
    if tree[root] != 0 and sec_l != sec_r:
        promise = tree[root]
        tree[root] = 0
        tree[root * 2 + 1] += promise
        tree[root * 2 + 2] += promise
    if sec_l == sec_r and ind == sec_l:
        return tree[root]
    if ind < sec_l or ind > sec_r:
        return -1
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    res_left = get_num(ind, tree, left_child_l, left_child_r, root * 2 + 1)
    if res_left == -1:
        right_child_l = (sec_l + sec_r) // 2 + 1
        right_child_r = sec_r
        return get_num(ind, tree, right_child_l, right_child_r, root * 2 + 2)
    return res_left


def update_numbers(l, r, add_value, tree, sec_l, sec_r, root=0):
    if tree[root] != 0 and sec_l != sec_r:
        promise = tree[root]
        tree[root] = 0
        tree[root * 2 + 1] += promise
        tree[root * 2 + 2] += promise
    if l <= sec_l and r >= sec_r:
        tree[root] += add_value
        return
    if r < sec_l or l > sec_r:
        return
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    update_numbers(l, r, add_value, tree, left_child_l, left_child_r, root * 2 + 1)
    right_child_l = (sec_l + sec_r) // 2 + 1
    right_child_r = sec_r
    update_numbers(l, r, add_value, tree, right_child_l, right_child_r, root * 2 + 2)
    return


n = int(input())
a = list(map(int, input().split()))
tree_sec, n_ = get_treeset(a)
m = int(input())
res = []
for _ in range(m):
    row = input().split()
    command = row[0].strip()
    if command == 'g':
        index = int(row[1])
        res.append(get_num(index - 1, tree_sec, 0, n_ - 1))
    else:
        left, right, value = map(int, row[1:])
        update_numbers(left - 1, right - 1, value, tree_sec, 0, n_ - 1)

print(*res, sep='\n')
