# В данном врианте выполнен только подсчет если нет обратных ребер (в графе один исток)

import sys


sys.setrecursionlimit(100000)


# Функция быстрого возведения в степень
def bin_pow(num, degree):
    if degree == 0:
        return 1
    elif degree % 2 == 0:
        return bin_pow((num * num) % m, degree // 2) % m
    else:
        return (num * bin_pow(num, degree - 1)) % m


# Функция обхода в глубину для подсчета размера поддерева и динамики кол-ва топсортов для отдельного графа без обратных ребер
def dfs_top_sort(root):
    if not tree[root]:
        dp_orient_graph[root] = (1, 1)
        return
    childs = [i for i in tree[root] if not dp_orient_graph[i]]
    for child in childs:
        dfs_top_sort(child)
    root_size = 1
    root_dp = 1
    znam = 1
    for child in childs:
        size, dp = dp_orient_graph[child]
        root_size += size
        root_dp = (root_dp * dp) % m
        znam = (znam * factorials_division[size]) % m
    root_dp = (factorials[root_size - 1] * znam * root_dp) % m
    dp_orient_graph[root] = (root_size, root_dp)
    return


n = int(input())
tree = [set() for _ in range(n + 1)]
parents = [set() for _ in range(n + 1)]
for _ in range(n - 1):
    first, second = map(int, input().split())
    tree[first].add(second)
    parents[second].add(first)
m = 1000000007

factorials = [1] * (n + 1)
factorials_division = [1] * (n + 1)
factorial = 1
factorial_pow = 1
for i in range(2, n + 1):
    factorial = (factorial * i) % m
    factorials[i] = factorial
    factorial_pow = (factorial_pow * bin_pow(i, m - 2)) % m
    factorials_division[i] = factorial_pow

# массив для подсчета динамики, без учета обратных ребер, считаем как для отдельных компонент,
# кладем размер поддерева и динамику подсчета топсортов
dp_orient_graph = [0] * (n + 1)
# в компонентах будем хранить размер дерева и подсчитанное кол-во топсортов для рута
components = []
for v in range(1, n + 1):
    if not parents[v] and not dp_orient_graph[v]:
        dfs_top_sort(v)
        components.append(dp_orient_graph[v])

if len(components) == 1:
    answer = components[0][1] % m
else:
    answer = factorials[n]
    for size, dp in components:
        answer = (answer * factorials_division[size] * dp) % m
    substr = 0 # количество неподходящих топсортов, излишне подсчитанных при учете нескольких деревьев как независимых
    answer -= substr

print(answer)
