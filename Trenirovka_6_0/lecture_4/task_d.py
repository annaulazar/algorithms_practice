import sys


sys.setrecursionlimit(100000)


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
    child_left = tree[1]
    if child_left is not None:
        PRINTTREE(child_left, level=level+1)
    print('.' * level, tree[0], sep='')
    child_right = tree[2]
    if child_right is not None:
        PRINTTREE(child_right, level=level + 1)


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
