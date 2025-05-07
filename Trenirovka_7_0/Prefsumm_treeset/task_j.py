def get_treeset(array):
    degree_two = 0
    while 2 ** degree_two < len(array):
        degree_two += 1
    size = 2 ** degree_two
    tree_set = [[0, 0, 0]] * (size * 2 - 1)  # [хэш, длина отрезка, обещание]
    for i in range(len(array)):
        tree_set[i + size - 1] = [array[i], 1, 0]
    for j in range(size - 2, -1, -1):
        left_child = tree_set[2 * j + 1]
        right_child = tree_set[2 * j + 2]
        hash_sec = (left_child[0] * x[right_child[1]] + right_child[0]) % p
        length_sec = left_child[1] + right_child[1]
        tree_set[j] = [hash_sec, length_sec, 0]

    return tree_set, size


def change_hash(ind, tree, value):
    if tree[ind][1] == 1:
        tree[ind][0] = value
    else:
        length_sec = tree[ind][1]
        tree[ind][0] = (pref_sum_x[length_sec] * value) % p
    tree[ind][2] = value


def get_hash_sec(left, right, tree, sec_l, sec_r, root=0):
    if tree[root][2]:
        promise = tree[root][2]
        tree[root][2] = 0
        if sec_l != sec_r:
            change_hash(root * 2 + 1, tree, promise)
            change_hash(root * 2 + 2, tree, promise)
    if left <= sec_l and right >= sec_r:
        return tree[root][:2]
    if right < sec_l or left > sec_r:
        return 0, 0
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    res_left = get_hash_sec(left, right, tree, left_child_l, left_child_r, root * 2 + 1)
    right_child_l = (sec_l + sec_r) // 2 + 1
    right_child_r = sec_r
    res_right = get_hash_sec(left, right, tree, right_child_l, right_child_r, root * 2 + 2)
    new_hash = (res_left[0] * x[res_right[1]] + res_right[0]) % p
    return new_hash, res_left[1] + res_right[1]


def update_sec(left, right, new_value, tree, sec_l, sec_r, root=0):
    if tree[root][2]:
        promise = tree[root][2]
        tree[root][2] = 0
        if sec_l != sec_r:
            change_hash(root * 2 + 1, tree, promise)
            change_hash(root * 2 + 2, tree, promise)
    if left <= sec_l and right >= sec_r:
        change_hash(root, tree, new_value)
        return tree[root][0]
    if right < sec_l or left > sec_r:
        return tree[root][0]
    left_child_l = sec_l
    left_child_r = (sec_l + sec_r) // 2
    res_left = update_sec(left, right, new_value, tree, left_child_l, left_child_r, root * 2 + 1)
    right_child_l = (sec_l + sec_r) // 2 + 1
    right_child_r = sec_r
    res_right = update_sec(left, right, new_value, tree, right_child_l, right_child_r, root * 2 + 2)
    right_length = tree[root * 2 + 2][1]
    new_hash = (res_left * x[right_length] + res_right) % p
    tree[root][0] = new_hash
    return new_hash


p = 10**9 + 7
x_ = 131
n = int(input())
a = list(map(int, input().split()))
x = [0] * (n + 1)
x[0] = 1
for i in range(1, n + 1):
    x[i] = (x[i - 1] * x_) % p
pref_sum_x = [0] * (n + 2)
for j in range(1, n + 2):
    pref_sum_x[j] = (pref_sum_x[j - 1] + x[j - 1]) % p

tree_hash_sec, n_ = get_treeset(a)

q = int(input())
res = []
for _ in range(q):
    t, l, r, k = map(int, input().split())
    if t == 0:
        update_sec(l - 1, r - 1, k, tree_hash_sec, 0, n_ - 1)
    else:
        first = get_hash_sec(l - 1, l + k - 2, tree_hash_sec, 0, n_ - 1)
        second = get_hash_sec(r - 1, r + k - 2, tree_hash_sec, 0, n_ - 1)
        if first == second:
            res.append('+')
        else:
            res.append('-')

print(''.join(res))
