M = int(input())
cards = list(map(int, input().split()))

cards_cost = []
for i in range(31):
    cards_cost.append([2 ** i / cards[i], cards[i], i]) # Себестоимость 1 сек, кол-во секунд, номер
cards_cost.sort()

res = 0
while M > 0:
    current_card = cards_cost[0]
    cnt = M // current_card[1]
    res += cnt * (2 ** current_card[2])
    M -= cnt * current_card[1]
    if M > 0:
        for i in range(31):
            card = cards_cost[i]
            if card[1] > M:
                card[0] = (2 ** card[2]) / M
                card[1] = M
        cards_cost.sort()

print(res)
