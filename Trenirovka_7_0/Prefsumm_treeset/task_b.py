def get_treeset(array):
    degree_two = 0
    while 2 ** degree_two < len(array):
        degree_two += 1
    size = 2 ** degree_two
    tree_set = [(-1, -1)] * (size * 2 - 1)  # (максимум, количество максимумов)
    for i in range(len(array)):
        tree_set[i + size - 1] = (array[i], i)
    for j in range(size - 2, -1, -1):
        left_child = tree_set[2 * j + 1]
        right_child = tree_set[2 * j + 2]
        if left_child[0] > right_child[0]:
            tree_set[j] = left_child
        else:
            tree_set[j] = right_child

    return tree_set, size


def get_ind_max(l, r, tree, sec_l, sec_r, root=0):
    if l <= sec_l and r >= sec_r:
        return tree[root]
    elif r < sec_l or l > sec_r:
        return (0, 0)
    else:
        left_child_l = sec_l
        left_child_r = (sec_l + sec_r) // 2
        res_left = get_ind_max(l, r, tree, left_child_l, left_child_r, root * 2 + 1)
        right_child_l = (sec_l + sec_r) // 2 + 1
        right_child_r = sec_r
        res_right = get_ind_max(l, r, tree, right_child_l, right_child_r, root * 2 + 2)
        if res_left[0] > res_right[0]:
            return res_left
        else:
            return  res_right


n = int(input())
a = list(map(int, input().split()))
tree_cnt_max, n_ = get_treeset(a)
k = int(input())
for _ in range(k):
    left, right = map(int, input().split())
    res = get_ind_max(left - 1, right - 1, tree_cnt_max, 0, n_ - 1)
    print(res[1] + 1)
