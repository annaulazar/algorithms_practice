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


# Функция обхода в глубину для подсчета максимальных глубин для поддеревьев, а также максимального пути для поддерева
# Возвращает только глубину
def get_depth_max_way(root: int):
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
                depth_max_ways[current] = (1, 0)
            else:
                child_depth: list = sorted(list(depth_max_ways[ch][0] for ch in tree[current]))
                depth = child_depth[-1] + 1
                if len(child_depth) >= 2:
                    max_way_temp = child_depth[-1] + child_depth[-2]
                else:
                    max_way_temp = child_depth[-1]
                max_way = max(max(depth_max_ways[ch][1] for ch in tree[current]), max_way_temp)
                depth_max_ways[current] = (depth, max_way)
            stack.pop()


# Функция обхода в ширину для динамического подсчета максимального пути до вершины через родителя
def get_parent_way(root: int):
    que = deque()
    que.append(root)
    while que:
        parent = que.popleft()
        child_depth = {child: depth_max_ways[child][0] for child in tree[parent]}
        for child in tree[parent]:
            max_other_child = max((child_depth[key] for key in child_depth if key != child), default=0)
            dp_parent_way[child] = max(dp_parent_way[parent], max_other_child) + 1
            que.append(child)


# Функция подсчета произведения ребер максимальных путей, образовавшихся в подграфах вершин u и v при удалени ребра u-v
def get_multiply_edges(v, u):
    if u in tree[v]:
        parent = v
        son = u
    else:
        parent = u
        son = v
    son_way = depth_max_ways[son][1]
    parent_child_depth: list = list(depth_max_ways[child][0] for child in tree[parent] if child != son)
    parent_child_depth.append(dp_parent_way[parent])
    parent_child_depth.sort()
    if len(parent_child_depth) >= 2:
        parent_way_temp = parent_child_depth[-1] + parent_child_depth[-2]
    else:
        parent_way_temp = parent_child_depth[-1]
    parent_way = max(max((depth_max_ways[child][1] for child in tree[parent] if child != son), default=0), parent_way_temp)
    return son_way * parent_way


n = int(input())
tree = [set() for _ in range(n + 1)]
edges = []
for _ in range(n - 1):
    first, second = map(int, input().split())
    tree[first].add(second)
    tree[second].add(first)
    edges.append((first, second))

visited = [0] * (n + 1)
dfs_tree(1)

# В массив складываем максимальную глубину для поддерева (расстояние до самого далекого листа),
# и максимальный путь для поддерева из данного узла
depth_max_ways = [(0, 0) for _ in range(n + 1)]
visited = [0] * (n + 1)
get_depth_max_way(1)

# Массив для динамического определения максимального пути для каждой вершины, проходящего через родителя
dp_parent_way = [0] * (n + 1)
get_parent_way(1)

answer = 0
for v, u in edges:
    temp = get_multiply_edges(v, u)
    answer = max(answer, temp)

print(answer)
