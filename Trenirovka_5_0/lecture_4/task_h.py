def lbinpoisk(l, r, level):
    while l < r:
        m = (l + r) // 2
        if votes[m][0] > level:
            r = m
        else:
            l = m + 1
    return l


def check_win(level, index):
    level_index = lbinpoisk(index, n - 1, level)
    taken = votes_suf[level_index] - level * (n - level_index)
    return votes[index][0] + taken > level, taken


def rbinpoisk(l, r, index):
    while l < r:
        m = (l + r + 1) // 2
        if check_win(m, index)[0]:
            l = m
        else:
            r = m - 1
    return r, check_win(r, index)[1]


n = int(input())
bribes = [0] * n # Стоимость подкупа партий
start_votes = [0] * n # Изначальное распределение голосов по партиям, для ответа, здесь в конце будем изменять количество голосов
votes = [] # (v, i) Голоса партий с их номером
for i in range(n):
    v, b = map(int, input().split())
    bribes[i] = b
    votes.append((v, i))
    start_votes[i] = v

# Сортируем по голосам, подсчитываем суффиксные суммы голосов, перебираем подходящие партии и с помощью бинпоиска находим уровень с которого нужно голоса более высоких партий отдать подходящей партии
votes.sort()
max_votes = votes[-1][0]
votes_suf = [0] * n
votes_suf[-1] = votes[-1][0]
for j in range(n - 2, -1, -1):
    votes_suf[j] = votes_suf[j + 1] + votes[j][0]

min_cost = 10 ** 7
result = [0, 0, 0, 0] # номер подходящей партии, количество голосов для победы, уровень отбора голосов, лишние голоса для возврата
for k in range(n):
    if bribes[votes[k][1]] != -1:
        if n == 1 or (k == n - 1 and votes[k - 1][0] < max_votes):
            level, cost, extra = votes[k][0], 0, 0
        else:
            level, taken_votes = rbinpoisk(votes[k][0], max_votes, k)
            if votes[k][0] + taken_votes - level >= 2:
                extra = votes[k][0] + taken_votes - (level + 2)
            elif taken_votes == 0:
                extra = -1
            else:
                extra = 0
            cost = taken_votes - extra
        if bribes[votes[k][1]] + cost < min_cost:
            min_cost = bribes[votes[k][1]] + cost
            result = [votes[k][1], cost, level, extra]

party, cost, level, extra = result
for p in range(n):
    if p == party:
        start_votes[p] += cost
    elif start_votes[p] > level and extra > 0:
        start_votes[p] = level + 1
        extra -= 1
    elif start_votes[p] == level and extra < 0:
        start_votes[p] = level - 1
        extra += 1
    elif start_votes[p] > level:
        start_votes[p] = level
print(cost + bribes[party])
print(party + 1)
print(*start_votes)
