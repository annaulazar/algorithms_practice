import sys


sys.setrecursionlimit(300000)


def get_sum_moneys(root):
    # Поддерживаем количество узлов в поддереве и накопленные монеты для текущего узла
    node = [1, 1]
    for sub in subords[root]:
        sub_node = get_sum_moneys(sub)
        node[1] += sub_node[0] + sub_node[1]
        node[0] += sub_node[0]
    moneys[root] = node[1]
    return node

n = int(input())
bosses = [int(x) for x in input().split()]
subords = [[] for _ in range(n + 1)]
for i in range(n - 1):
    subords[bosses[i]].append(i + 2)
moneys = [1] * (n + 1)
get_sum_moneys(1)
print(*moneys[1:])
