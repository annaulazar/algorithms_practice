import sys

sys.setrecursionlimit(200000)

n = int(input())
lists = {}
sublists = {}


def create_list(name: str, values: str):
    nums = values.split(',')
    lists[name] = nums


def create_sublist(name: str, parent: str, left: int):
    if parent in lists:
        sublists[name] = (parent, left)
    else:
        pra_parent = sublists[parent][0]
        left = left + sublists[parent][1] - 1
        sublists[name] = (pra_parent, left)


def add_elem(name: str, elem: str):
    lists[name].append(elem)


def get_elem(name: str, ind: int):
    if name in lists:
        return lists[name][ind - 1]
    parent = sublists[name][0]
    ind = ind + sublists[name][1] - 1
    return lists[parent][ind - 1]


def set_elem(name: str, ind: int, value: str):
    if name in lists:
        lists[name][ind - 1] = value
    else:
        parent = sublists[name][0]
        ind = ind + sublists[name][1] - 1
        lists[parent][ind - 1] = value


for _ in range(n):
    command = input().strip()
    if command.startswith('List ') or command.startswith('list '):
        first, second = command.split('=')
        name = first.split()[1]
        if second.startswith(' new List(') or second.startswith(' new list('):
            values = second.split('(')[-1].split(')')[0]
            create_list(name, values)
        else:
            parent, sub = second.strip().split('.')
            left, right = map(int, sub.split('(')[-1].split(')')[0].split(','))
            create_sublist(name, parent, left)
    else:
        name, sub_com = command.split('.')
        args = sub_com.split('(')[-1].split(')')[0]
        if sub_com.startswith('get('):
            ind = int(args)
            print(get_elem(name, ind))
        elif sub_com.startswith('set('):
            args = args.split(',')
            ind = int(args[0])
            value = args[1]
            set_elem(name, ind, value)
        elif sub_com.startswith('add('):
            add_elem(name, args)
