# 3-правильная очередь
# XY, XZ, YZ - правильные пары
# По набору символов определить можно ли составить правильные пары


# По сути 2 прохода вперед и назад, но немного замудренно
def check_reverse(queue):
    x, y = 0, 0
    for i in range(len(queue) - 1, -1, -1):
        if queue[i] == "X":
            x += 1
        elif queue[i] == "Y" or queue[i] == "Z":
            y += 1
        if x > y:
            return False
    return True


def check_queue(queue: str, pos=0, x=0, y=0) -> bool:
    while pos < len(queue):
        if queue[pos] == "X":
            x += 1
            pos += 1
        elif queue[pos] == "Y":
            y += 1
            pos += 1
        elif queue[pos] == "Z" and y > 0:
            y -= 1
            pos += 1
        elif queue[pos] == "Z" and y == 0 and x > 0:
            x -= 1
            pos += 1
        elif queue[pos] == "Z" and y == 0 and x == 0:
            return False
    print(x, y)
    if x == 0 and y == 0:
        return True
    if x%2 == y%2:
        return check_reverse(queue)
    return False


for _ in range(int(input())):
    n = int(input())
    q = input().strip()
    if n % 2:
        res = False
    else:
        res = check_queue(q)
    print(['No', 'Yes'][res])
