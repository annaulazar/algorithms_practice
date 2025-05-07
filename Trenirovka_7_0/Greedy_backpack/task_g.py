def restoring_answer(full_bags, index) -> []:
    res = []
    for color, bag in enumerate(full_bags):
        current_index = index
        while current_index > 0:
            append_brick = bag[current_index]
            res.append(append_brick)
            current_index -= bricks[color][append_brick]
    return res


n, k = map(int, input().split())
bricks = [{} for _ in range(k)]
color_lengths = [0] * k
for i in range(1, n + 1):
    length, color = map(int, input().split())
    bricks[color - 1][i] = length
    color_lengths[color - 1] += length

size = max(color_lengths)
bags = [[0] + [-1] * size for _ in range(k)]

for color, bricks_color in enumerate(bricks):
    last_ind = 0
    for brick_number, brick_length in bricks_color.items():
        start_ind = min(last_ind, size + 1 - brick_length)
        last_ind = start_ind + brick_length
        for ind in range(start_ind, -1, -1):
            if bags[color][ind] != -1:
                target_ind = ind + brick_length
                if bags[color][target_ind] == -1:
                    bags[color][target_ind] = brick_number

for j in range(1, size):
    if all([bags[color][j] != -1 for color in range(k)]):
        print('YES')
        print(*restoring_answer(bags, j))
        break
else:
    print('NO')

