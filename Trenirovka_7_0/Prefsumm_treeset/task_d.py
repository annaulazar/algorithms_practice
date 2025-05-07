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


def get_max(l, r, tree, sec_l, sec_r, root=0):
    if l <= sec_l and r >= sec_r:
        return tree[root]
    elif r < sec_l or l > sec_r:
        return -1
    else:
        left_child_l = sec_l
        left_child_r = (sec_l + sec_r) // 2
        res_left = get_max(l, r, tree, left_child_l, left_child_r, root * 2 + 1)
        right_child_l = (sec_l + sec_r) // 2 + 1
        right_child_r = sec_r
        res_right = get_max(l, r, tree, right_child_l, right_child_r, root * 2 + 2)
        return max(res_left, res_right)


def update_number(ind, new_value, tree):
    tree[ind] = new_value
    parent = (ind - 1) // 2
    while parent >= 0:
        left_child = tree[2 * parent + 1]
        right_child = tree[2 * parent + 2]
        tree[parent] = max(left_child, right_child)
        parent = (parent - 1) // 2


n = int(input())
a = list(map(int, input().split()))
tree_max, n_ = get_treeset(a)
k = int(input())
res = []
for _ in range(k):
    row = input().split()
    command = row[0].strip()
    first = int(row[1])
    second = int(row[2])
    if command == 's':
        res.append(get_max(first - 1, second - 1, tree_max, 0, n_ - 1))
    else:
        update_number(first - 1 + n_ - 1, second, tree_max)

print(*res)
