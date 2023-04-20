# Дано неориентированное дерево, подвешенное за вершину 1. Для каждой вершины подсчитайте, сколько вершин содержится
# в поддереве, подвешенном за данную вершину.
import sys

sys.setrecursionlimit(100000)


# рекурсивня функция обхода дерева с вершины для подсчета размера всех поддеревьев
def dfs(now, neighbours, subtrees):
    subtrees[now] = 1  # Текущей вершине присваиваем 1
    for neighbour in neighbours[now]:  # Обходим всех соседей текущей вершины
        if subtrees[neighbour] == -1:  # признак, что сосед еще не был обойден и является потомком
            subtrees[now] += dfs(neighbour, neighbours, subtrees)  # присоединяем к вершине сумму размера потомка
    return subtrees[now]  # возврат не обязателен, так как меняем глобальный массив


n = int(input())
tree = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = (int(x) for x in input().split())
    tree[a].append(b)
    tree[b].append(a)

subTreeSize = [-1] * (n + 1)  # -1 признак не обойденной вершины
dfs(1, tree, subTreeSize)  # рекурсивня функция обхода дерева с вершины, изначальная вершина 1
print(*subTreeSize[1:])
