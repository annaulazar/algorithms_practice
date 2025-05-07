from collections import deque


# Функция обхода в глубину для того, чтобы оставить в множестве cocедей только детей
def dfs_tree(root: int):
    visited[root] = 1
    stack = [(neib, root) for neib in tree[root]]
    while stack:
        neib, prev = stack.pop()
        if visited[neib]:
            tree[prev].remove(neib)
        else:
            visited[neib] = 1
            for next_neib in tree[neib]:
                stack.append((next_neib, neib))


# Функция обхода в глубину для подсчета динамики
def dfs_dinamic(root: int):
    visited[root] = 1
    stack = [root]
    while stack:
        current: int = stack[-1]
        flag_childs = False
        for child in tree[current]:
            if not visited[child]:
                visited[child] = 1
                stack.append(child)
                flag_childs = True
        if not flag_childs:
            if not tree[current]:
                dp[0][current] = 0
                dp[1][current] = a[current - 1]
            else:
                sum_for_0 = 0
                sum_for_1 = 0
                for child in tree[current]:
                    sum_for_0 += dp[1][child]
                    sum_for_1 += min(dp[0][child], dp[1][child])
                dp[0][current] = sum_for_0
                dp[1][current] = a[current - 1] + sum_for_1
            stack.pop()


def dfs_recovery(root, color):
    que = deque()
    for child in tree[root]:
        que.append((child, color))
    while que:
        temp, temp_color = que.popleft()
        if temp_color == 0 or dp[1][temp] < dp[0][temp]:
            colored[temp] = 1
            new_color = 1
        else:
            new_color = 0
        for temp_child in tree[temp]:
            que.append((temp_child, new_color))


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    first, second = map(int, input().split())
    tree[first].append(second)
    tree[second].append(first)
a = list(map(int, input().split()))

visited = [0] * (n + 1)
dfs_tree(1)

if n == 1:
    answer = a[0]
    cnt = 1
    numbers = [1]
else:
    dp = [[0] * (n + 1) for _ in range(2)]
    visited = [0] * (n + 1)
    dfs_dinamic(1)

    colored = [0] * (n + 1)
    if dp[0][1] < dp[1][1]:
        answer = dp[0][1]
        dfs_recovery(1, 0)
    else:
        answer = dp[1][1]
        colored[1] = 1
        dfs_recovery(1, 1)

    numbers = [ind for ind, value in enumerate(colored) if value]
    cnt = len(numbers)

print(answer, cnt)
print(*numbers)
