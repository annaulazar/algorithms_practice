
def check_win(player, last_move):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        for i in range(1, 5):
            if (last_move[0] + dx * i, last_move[1] + dy * i) in player:
                count += 1
            else:
                break
        for i in range(1, 5):
            if (last_move[0] - dx * i, last_move[1] - dy * i) in player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False


n = int(input().strip())
steps = []
for i in range(n):
    steps.append(tuple(map(int, input().split())))
players = [{}, {}]
winner = None
for i, (x, y) in enumerate(steps):
    current_player = i % 2
    players[current_player][(x, y)] = True
    if i >= 9 and check_win(players[current_player], (x, y)):
        winner = "First" if current_player == 0 else "Second"
        break
if winner:
    if i + 1 < len(steps):
        print("Inattention")
    else:
        print(winner)
else:
    print("Draw")
