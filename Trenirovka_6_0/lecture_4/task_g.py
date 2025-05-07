import sys


sys.setrecursionlimit(1000000)


# Решение с рекурсией не проходит по памяти. В файле -1 заменила рекурсию на с тэк в функции обхода в глубину
# Функция обхода в глубину для того, чтобы оставить в множестве друзей только потомков и обнаружить цикл, если есть
def dfs_and_circle(root: int, prev=0):
    visited[root] = 1
    friends = birds[root].copy()
    for friend in friends:
        if friend != prev and visited[friend] == 1:
            return True
        if visited[friend]:
            birds[root].remove(friend)
        else:
            if dfs_and_circle(friend, root):
                return True
    return False


def get_cnt_with_friends(root, valid_cnt):
    ans = 1
    friends_with_childs = []
    cnt_without_childs = 0
    for friend in birds[root]:
        if birds[friend]:
            friends_with_childs.append(friend)
        else:
            cnt_without_childs += 1
    if len(friends_with_childs) > valid_cnt:
        return 0, []
    for i in range(2, cnt_without_childs + 1):
        ans = (ans * i) % k
    return ans, friends_with_childs


# Функция обхода в ширину для подсчета количества вариантов для размещения дружелюбных птиц
def bfs(root: int):
    if len(birds[root]) == 1:
        new_root = birds[root].pop()
        birds[new_root].add(root)
        root = new_root
    flag_multy = False
    ans, friends_with_childs = get_cnt_with_friends(root, 2)
    for friend in friends_with_childs:
        flag_multy = True
        current = friend
        while birds[current]:
            temp_ans, temp_friends_with_childs = get_cnt_with_friends(current, 1)
            ans = (ans * temp_ans) % k
            if not temp_friends_with_childs:
                break
            current = temp_friends_with_childs[0]
    if flag_multy:
        return ans * 2
    return ans


n, m, k = map(int, input().split())
birds = [set() for _ in range(n + 1)]
free = [1] * (n + 1)
free[0] = 0
for _ in range(m):
    first, second = map(int, input().split())
    birds[first].add(second)
    birds[second].add(first)
    free[first] = 0
    free[second] = 0
cnt_free = sum(free)


visited = [0] * (n + 1)
roots = []
for i in range(1, n + 1):
    if not visited[i] and not free[i]:
        roots.append(i)
        if dfs_and_circle(i):
            res = 0
            break
else:
    res = 1
    for root in roots:
        res = (res * bfs(root)) % k

    for x in range(len(roots)):
        res = (res * (x + 1) * 2) % k

    for j in range((n - cnt_free + 2), n + 2):
        res = (res * j) % k

print(res)
