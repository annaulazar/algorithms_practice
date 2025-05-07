def find_root(x):
    if x == islands[x][0]:
        return x
    root = find_root(islands[x][0])
    islands[x][0] = root
    return root


def merge_sets(x, y):
    x = find_root(x)
    y = find_root(y)
    if islands[y][1] > islands[x][1]:
        x, y = y, x
    if x != y:
        islands[y][0] = x
        islands[x][1] += islands[y][1]


n, m = map(int, input().split())
#корень и размер множества
islands = {i: [i, 1] for i in range(1, n + 1)}
cnt = n
answer = 0
while cnt > 1 and answer < m:
    first, second = map(int, input().split())
    if first == second:
        answer += 1
        continue
    if find_root(first) != find_root(second):
        merge_sets(first, second)
        cnt -= 1
    answer += 1

print(answer)
