def find_root(x):
    if x == graph[x][0]:
        return x
    root = find_root(graph[x][0])
    graph[x][0] = root
    return root


def merge_sets(x, y):
    x = find_root(x)
    y = find_root(y)
    if graph[y][1] > graph[x][1]:
        x, y = y, x
    if x != y:
        graph[y][0] = x
        graph[x][1] += graph[y][1]


n, m, k = map(int, input().split())
#корень и размер множества
graph = {i: [i, 1] for i in range(1, n + 1)}
for _ in range(m):
    v1, v2 = map(int, input().split())
operations = []
for _ in range(k):
    row = input().split()
    first, second = map(int, row[1:])
    operations.append((row[0], first, second))
answer = []
while operations:
    command, vertex1, vertex2 = operations.pop()
    if command == 'ask':
        answer.append(['NO', 'YES'][find_root(vertex1) == find_root(vertex2)])
    else:
        merge_sets(vertex1, vertex2)
for i in range(len(answer) - 1, -1, -1):
    print(answer[i])
