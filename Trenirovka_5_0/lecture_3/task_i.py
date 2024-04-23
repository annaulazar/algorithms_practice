def parse_match(row: str) -> tuple[str, int, str, int]:
    row = row.split('-')
    com1 = row[0].rstrip()[1:-1]
    com2, score = row[1].rsplit(maxsplit=1)
    com2 = com2.strip()[1:-1]
    a, b = map(int, score.split(':'))
    return com1, a, com2, b


def parse_player(row: str, command: str, index: int) -> None:
    player, minute = row.rsplit(maxsplit=1)
    player = player.strip()
    minute = int(minute[:-1])
    if player not in player_comand:
        player_comand[player] = command
    if player not in players:
        players[player] = [0, 0, [0] * 91]
    players[player][1] += 1
    players[player][2][minute] += 1
    if index == 0:
        first_goal.append((minute, player))


def set_first_goal() -> None:
    first_goal.sort()
    if first_goal:
        _, player = first_goal[0]
        players[player][0] += 1
        commands[player_comand[player]][0] += 1


def match_score(com1, com2, gol1, gol2):
    for command, goals in zip((com1, com2), (gol1, gol2)):
        if command not in commands:
            commands[command] = [0, 0, 0]
        commands[command][1] += goals
        commands[command][2] += 1


def get_total_goals(reqwest: str) -> None:
    if reqwest.endswith('"'):
        index = reqwest.find('"')
        command = reqwest[index + 1:-1]
        res = 0
        if command in commands:
            res = commands[command][1]
        print(res)
    else:
        index = reqwest.find('by')
        player = reqwest[index + 3:]
        res = 0
        if player in players:
            res = players[player][1]
        print(res)


def get_mean_goals(reqwest: str) -> None:
    if reqwest.endswith('"'):
        index = reqwest.find('"')
        command = reqwest[index + 1:-1]
        print(commands[command][1] / commands[command][2])
    else:
        index = reqwest.find('by')
        player = reqwest[index + 3:]
        command = player_comand[player]
        print(players[player][1] / commands[command][2])


def get_goals_by_minutes(reqwest: str) -> None:
    index = reqwest.find('by')
    player = reqwest[index + 3:]
    if player not in players:
        print(0)
        return
    last_index = reqwest.find('minutes')
    first_index = reqwest.find('first')
    if first_index != -1:
        first_index += 6
        minutes = int(reqwest[first_index: last_index - 1])
        print(sum(players[player][2][: minutes + 1]))
        return
    first_index = reqwest.find('last')
    if first_index != -1:
        first_index += 5
        minutes = int(reqwest[first_index: last_index - 1])
        print(sum(players[player][2][-minutes:]))
        return
    first_index = reqwest.find('minute') + 7
    minute = int(reqwest[first_index: index - 1])
    print(players[player][2][minute])


def get_first_goals(reqwest: str) -> None:
    if reqwest.endswith('"'):
        index = reqwest.find('"')
        command = reqwest[index + 1:-1]
        res = 0
        if command in commands:
            res = commands[command][0]
        print(res)
    else:
        index = reqwest.find('by')
        player = reqwest[index + 3:]
        res = 0
        if player in players:
            res = players[player][0]
        print(res)


def get_answer(reqwest: str) -> None:
    if reqwest.startswith('Total'):
        get_total_goals(reqwest)
    elif reqwest.startswith('Mean'):
        get_mean_goals(reqwest)
    elif reqwest.startswith('Goals'):
        get_goals_by_minutes(reqwest)
    elif reqwest.startswith('Score'):
        get_first_goals(reqwest)


# Структура для игроков {Игрок 1: [открыл счет, всего голов, [0]*91 - голы для каждой минуты]}
players = {}
# В какой команде играет игрок {Игрок 1: Команда 1}
player_comand = {}
# Структура для команд {Команда 1: [открыла счет, всего голов, всего матчей]}
commands = {}

with open('input.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        if line.startswith('"'):
            command1, goals1, command2, goals2 = parse_match(line)
            match_score(command1, command2, goals1, goals2)
            first_goal = []
            for i in range(goals1):
                line = file.readline().strip()
                parse_player(line, command1, i)
            for j in range(goals2):
                line = file.readline().strip()
                parse_player(line, command2, j)
            set_first_goal()
        else:
            get_answer(line)
        line = file.readline().strip()
