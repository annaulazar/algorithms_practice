parents = {}

with open('input.txt') as file:
    n = int(file.readline().strip())
    for _ in range(n - 1):
        son, parent = file.readline().strip().split()
        parents[son] = parent
    for row in file.readlines():
        first, second = row.strip().split()
        first_parents = {first}
        while first in parents:
            first = parents[first]
            first_parents.add(first)
        while second in parents or second in first_parents:
            if second in first_parents:
                print(second)
                break
            second = parents[second]
