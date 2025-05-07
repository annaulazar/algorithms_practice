import sys

sys.setrecursionlimit(100000)


def get_sum_desc(root):
    if not childs[root]:
        descendants[root] = 0
        return 0
    else:
        res = len(childs[root])
        for son in childs[root]:
            res += get_sum_desc(son)
        descendants[root] = res
        return res


n = int(input())
childs = {}
parents = set()
sons = set()
for _ in range(n - 1):
    son, parent = input().strip().split()
    if parent not in childs:
        childs[parent] = []
    childs[parent].append(son)
    if son not in childs:
        childs[son] = []
    sons.add(son)
    if parent not in sons:
        parents.add(parent)
    if son in parents:
        parents.remove(son)
descendants = {}
get_sum_desc(parents.pop())
for key in sorted(descendants):
    print(key, descendants[key])
