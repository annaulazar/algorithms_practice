import sys


sys.setrecursionlimit(500000)


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
    childs = []
    for neib in tree[root]:
        if not dp_orient_graph[neib]:
            childs.append(neib)
        else:
            rever[neib].add(root) # если встречаем обратное ребро, добавляем его в отдельный массив
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


# Функция обхода в глубину для подсчета включений-исключений при обработке перевернутых ребер
def dfs_incl_exp(root):
    if not tree[root] and not rever[root]:
        dp_incl_excp[root][1][0] = 1
        dp_incl_excp[root][1][1] = 1
        return [1]
    childs = tree[root]
    revers_childs = rever[root]
    root_sizes = []
    root_dp_0 = []
    root_dp_1 = []
    znam = []
    for child in childs:
        sizes = dfs_incl_exp(child)
        if not root_sizes:
            root_sizes = [x + 1 for x in sizes]
            root_dp_0 = [dp_incl_excp[child][size][0] for size in sizes]
            root_dp_1 = [dp_incl_excp[child][size][1] for size in sizes]
            znam = [1 * factorials_division[size] for size in sizes]
        else:
            root_sizes = [x + y for x in root_sizes for y in sizes]
            root_dp_0 = [dp0 * dp_incl_excp[child][size][0] for dp0 in root_dp_0 for size in sizes]
            root_dp_1 = [dp1 * dp_incl_excp[child][size][1] for dp1 in root_dp_1 for size in sizes]
            znam = [zn * factorials_division[size] for zn in znam for size in sizes]
    if not revers_childs:
        for i in range(len(root_sizes)):
            dp_incl_excp[root][root_sizes[i]][0] = (factorials[root_sizes[i] - 1] * znam[i] * root_dp_0[i]) % m
            dp_incl_excp[root][root_sizes[i]][0] = (factorials[root_sizes[i] - 1] * znam[i] * root_dp_1[i]) % m
        return root_sizes
    for revers_child in revers_childs:
        sizes_reverse_child = dfs_incl_exp(revers_child)
        for i in range(len(root_sizes)):
            for size_reverse_child in sizes_reverse_child:
                root_size_with_reverse_child = root_sizes[i] + size_reverse_child
                dp_incl_excp[root][root_size_with_reverse_child][0] = ((((dp_incl_excp[root][root_sizes[i]][1] *
                                                                         factorials[root_size_with_reverse_child - 1]) % m *
                                                                       factorials_division[root_sizes[i] - 1]) % m *
                                                                        factorials_division[size_reverse_child]) % m *
                                                                       dp_incl_excp[revers_child][size_reverse_child][1]) % m
                dp_incl_excp[root][root_size_with_reverse_child][1] = ((((dp_incl_excp[root][root_sizes[i]][0] *
                                                                         factorials[root_size_with_reverse_child - 1]) % m *
                                                                        factorials_division[root_sizes[i] - 1]) % m *
                                                                       factorials_division[size_reverse_child]) % m *
                                                                       dp_incl_excp[revers_child][size_reverse_child][0]) % m

                dp_incl_excp[root][root_sizes[i]][1] = ((((dp_incl_excp[root][root_sizes[i]][0] *
                                                                         factorials[root_size_with_reverse_child]) % m *
                                                                        factorials_division[size_reverse_child]) % m *
                                                                       factorials_division[root_sizes[i]]) % m ) % m
                dp_incl_excp[root][root_sizes[i]][0] = ((((dp_incl_excp[root][root_sizes[i]][1] *
                                                           factorials[root_size_with_reverse_child]) % m *
                                                          factorials_division[size_reverse_child]) % m *
                                                         factorials_division[root_sizes[i]]) % m) % m
        return root_sizes + [x + y for x in root_sizes for y in sizes_reverse_child]


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
# массив для обратных ребер
rever = [set() for _ in range(n + 1)]
for v in range(1, n + 1):
    if not parents[v] and not dp_orient_graph[v]:
        dfs_top_sort(v)
        components.append(dp_orient_graph[v])

if len(components) == 1:
    answer = components[0][1] % m
else:
    answer = factorials[n]
    for comp_size, dp in components:
        answer = (answer * factorials_division[comp_size] * dp) % m
    # массив для подсчета динамики включений-исключений, размер и кол-во топсортов
    dp_incl_excp = [[[1] * 2 for _ in range(n + 1)] for y in range(n + 1)]
    dfs_incl_exp(1)
    if dp_incl_excp[1][n][1] > 1:
        answer -= dp_incl_excp[1][n][1]
    if dp_incl_excp[1][n][0] > 1:
        answer += dp_incl_excp[1][n][0]
    answer = answer % m

print(answer)
