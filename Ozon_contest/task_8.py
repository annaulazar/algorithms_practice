# Пример теста 1
# Входные данные
# 4
# 2
# TS TC
# AD AH
# 3
# 2H 3H
# 9S 9C
# 4D QS
# 3
# 4C 7H
# 4H 4D
# 6S 6H
# 3
# 2S 3H
# 2C 2D
# 3C 3D
# Выходные данные
# 2
# TD
# TH
# 0
# 3
# 7S
# 7C
# 7D
# 0

def get_combination(c1, c2, c3):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6' : 6, '7': 7, '8' : 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if c1[0] == c2[0] == c3[0]:
        combination = 3
        value = values[c1[0]]
    elif c1[0] == c2[0] or c1[0] == c3[0]:
        combination = 2
        value = values[c1[0]]
    elif c2[0] == c3[0]:
        combination = 2
        value = values[c2[0]]
    else:
        combination = 1
        value = max(values[c1[0]], values[c2[0]], values[c3[0]])
    return combination, value


def clean_cards():
    for key in cards:
        cards[key] = 0


rungs = '23456789TJQKA'
suits = 'SCDH'
cards = {}
for rung in rungs:
    for suit in suits:
        cards[rung + suit] = 0

all_res = []
n = int(input())
for z in range(n):
    k = int(input())
    players = []
    for i in range(k):
        card1, card2 = input().split()
        cards[card1], cards[card2] = 1, 1
        players.append((card1, card2))
    res = []
    for card in cards:
        if cards[card] == 0:
            first_combination = get_combination(*players[0], card)
            for j in range(1, k):
                if get_combination(*players[j], card) > first_combination:
                    break
            else:
                res.append(card)
    print(len(res))
    if len(res):
        print(*res, sep='\n', end='\n')

    if z != n -1:
        clean_cards()

#     all_res.append(str(len(res)))
#     all_res.extend(res)
#
# ref = []
# with open('3.a') as file:
#     for line in file:
#         ref.append(line.strip())
#
# for x in range(1, len(ref) + 1):
#     if ref[x] != all_res[x]:
#         print(x)
#         break
