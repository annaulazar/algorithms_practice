def get_levels(root, level):
    levels[root] = level
    for son in childs[root]:
        get_levels(son, level + 1)

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
levels = {}
get_levels(parents.pop(), 0)
for key in sorted(levels):
    print(key, levels[key])
