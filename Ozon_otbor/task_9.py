# 3-правильная очередь
# XY, XZ, YZ - правильные пары
# По набору символов определить можно ли составить правильные пары

# Перебор вариантов с рекурсией, неэффективное
def check_queue(queue: str, pos=0, x=0, y=0) -> bool:
    while pos < len(queue):
        if queue[pos] == "X":
            x += 1
            pos += 1
        elif queue[pos] == "Y" and x == 0:
            y += 1
            pos += 1
        elif queue[pos] == "Z" and x == 0 and y > 0:
            y -= 1
            pos += 1
        elif queue[pos] == "Z" and y == 0 and x > 0:
            x -= 1
            pos += 1
        elif queue[pos] == "Z" and y == 0 and x == 0:
            return False
        elif queue[pos] == "Y":
            temp_pos, temp_x, temp_y = pos, x, y
            x -= 1
            if check_queue(queue, pos + 1, x, y):
                return True
            x = temp_x
            y = temp_y + 1
            pos = temp_pos + 1
        elif queue[pos] == "Z":
            temp_pos, temp_x, temp_y = pos, x, y
            x -= 1
            if check_queue(queue, pos + 1, x, y):
                return True
            x = temp_x
            y = temp_y - 1
            pos = temp_pos + 1
    if x == 0 and y == 0:
        return True
    return False


for _ in range(int(input())):
    n = int(input())
    q = input().strip()
    res = check_queue(q)
    print(['No', 'Yes'][res])
