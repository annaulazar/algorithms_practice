'''У вас есть 1000$, которую вы планируете эффективно вложить. Вам даны цены за 1000 кубометров газа за n дней.
Можно один раз купить газ на все деньги в день i и продать его в один из последующих дней j, i < j.
Определите номера дней для покупки и продажи газа для получения максимальной прибыли.'''

# from random import randint

def my_function(n: int, price: list):
    minindex = 0
    cost = price[0]
    prib = 1
    answer = (0, 0)
    for i in range(1, n):
        if price[i] / cost > prib:
            prib = price[i] / cost
            answer = (minindex + 1, i + 1)
        if price[i] < cost:
            cost = price[i]
            minindex = i
    return answer


def teacher_function(n: int, cost: list):
    minindex = 0
    max_gaz = 1 / cost[0]
    prib = 0
    answer = (0, 0)
    for i in range(1, n):
        if max_gaz * cost[i] - 1 > prib:
            prib = max_gaz * cost[i] - 1
            answer = (minindex + 1, i + 1)
        if 1 / cost[i] > max_gaz:
            minindex = i
            max_gaz = 1 / cost[i]
    return answer


def best_function(n, cost):
    best_buy_day = best_sell_day = min_cost_day = 0
    for i in range(1, n):
        if cost[best_sell_day] * cost[min_cost_day] < cost[best_buy_day] * cost[i]:
            best_buy_day = min_cost_day
            best_sell_day = i
        if cost[min_cost_day] > cost[i]:
            min_cost_day = i
    if best_buy_day == best_sell_day:
        return 0, 0
    return best_buy_day + 1, best_sell_day + 1


k = int(input())
costs = [int(i) for i in input().split()]
print(*best_function(k, costs))

'''while True:
    n = 10
    rand_list = []
    for i in range(n):
        rand_list.append(randint(1, 100))
    my_ans = my_function(n, rand_list)
    t_ans = teacher_function(n, rand_list)
    if my_ans != t_ans:
        print(*rand_list)
        print(my_ans, t_ans)
        break'''
