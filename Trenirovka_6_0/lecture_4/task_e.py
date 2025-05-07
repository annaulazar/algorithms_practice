import sys


sys.setrecursionlimit(100000)


def get_tree_size(root: int):
    visited[root] = 1
    if not neighbors[root]:
        return 0
    else:
        res = 0
        for neib in neighbors[root]:
            if not visited[neib]:
                res += 1 + get_tree_size(neib)
        tree_size[root] += res
        return res


n = int(input())
neighbors = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    first, second = map(int, input().split())
    neighbors[first].append(second)
    neighbors[second].append(first)
visited = [0] * (n + 1)
tree_size = [1] * (n + 1)
get_tree_size(1)
print(*tree_size[1:])
