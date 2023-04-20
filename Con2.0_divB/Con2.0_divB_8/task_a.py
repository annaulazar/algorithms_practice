# Напишите программу, которая будет реализовывать действия в бинарном дереве поиска «вставить» и «найти»
# (по значению). Программа должна обрабатывать запросы трёх видов:
# ADD n — если указанного числа еще нет в дереве, вставлять его и выводить слово «DONE», если уже есть — оставлять
# дерево как было и выводить слово «ALREADY».
# SEARCH — следует выводить слово «YES» (если значение найдено в дереве) или слово «NO» (если не найдено).
# Дерево при этом не меняется.
# PRINTTREE — выводить все дерево, обязательно используя алгоритм, указанный в формате вывода результатов.
# Формат ввода
# В каждой строке входных данных записан один из запросов ADD n или SEARCH n или PRINTTREE. Гарантируется,
# что запросы PRINTTREE будут вызываться только в моменты, когда дерево не пустое. Общее количество запросов
# не превышает 1000, из них не более 20 запросов PRINTTREE.
# Формат вывода
# Для каждого запроса выводите ответ на него. Для запросов ADD и SEARCH — соответствующее слово в отдельной строке.
# На запрос PRINTTREE надо выводить дерево, обязательно согласно такому алгоритму:
# 1) Распечатать левое поддерево
# 2) Вывести количество точек, равное глубине узла
# 3) Вывести значение ключа
# 4) Распечатать правое поддерево


def create_node(tree, index, key):
    tree[index] = [key, None, None]


def ADD(tree, x):
    if tree[0] == 0:
        tree[0] = x
    else:
        key = tree[0]
        if x < key:
            if tree[1] is None:
                create_node(tree, 1, x)
            else:
                ADD(tree[1], x)
        elif x > key:
            if tree[2] is None:
                create_node(tree, 2, x)
            else:
                ADD(tree[2], x)


def SEARCH(tree, x):
    key = tree[0]
    if x == key:
        return True
    elif x < key:
        left = tree[1]
        if left is None:
            return False
        return SEARCH(left, x)
    elif x > key:
        right = tree[2]
        if right is None:
            return False
        return SEARCH(right, x)


def PRINTTREE(tree, level=0):
    print('.' * level, tree[0], sep='')
    for child in tree[1:]:
        if child is not None:
            PRINTTREE(child, level=level+1)

if __name__ == '__main__':
    main_tree = [0, None, None]
    with open('input.txt', encoding='utf-8') as file:
        for line in file:
            comand_num = line.split()
            comand = comand_num[0]
            if len(comand_num) > 1:
                num = int(comand_num[1])
            if comand == 'ADD':
                if SEARCH(main_tree, num):
                    print('ALREADY')
                else:
                    ADD(main_tree, num)
                    print('DONE')
            elif comand == 'SEARCH':
                print(['NO', 'YES'][SEARCH(main_tree, num)])
            elif comand == 'PRINTTREE':
                PRINTTREE(main_tree)
