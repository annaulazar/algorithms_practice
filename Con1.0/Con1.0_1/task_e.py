# Бригада скорой помощи выехала по вызову в один из отделенных районов. К сожалению, когда диспетчер получил
# вызов, он успел записать только адрес дома и номер квартиры K1, а затем связь прервалась. Однако он вспомнил,
# что по этому же адресу дома некоторое время назад скорая помощь выезжала в квартиру K2, которая расположена
# в подъезда P2 на этаже N2. Известно, что в доме M этажей и количество квартир на каждой лестничной площадке одинаково.
# Напишите программу, которая вычилсяет номер подъезда P1 и номер этажа N1 квартиры K1.
from random import randint

k1, m, k2, p2, n2 = (int(i) for i in input().split())


def get_p_n(k, m, apparts_floor):
    p = (k - 1) // (apparts_floor * m) + 1
    n = (k - (p - 1) * apparts_floor * m - 1) // apparts_floor + 1
    return p, n


def decision_1(k1, m, k2, p2, n2):
    results_p = set()
    results_n = set()
    apparts_floor = 1
    while apparts_floor * (m * (p2 - 1) + (n2 - 1)) < k2 and apparts_floor < 100000:
        p, n = get_p_n(k2, m, apparts_floor)
        if p2 == p and n2 == n:
            p1, n1 = get_p_n(k1, m, apparts_floor)
            results_p.add(p1)
            results_n.add(n1)
        apparts_floor += 1

    if len(results_p) == 0:
        return -1, -1
    else:
        return (0 if len(results_p) > 1 else results_p.pop(),
                1 if m == 1 else (0 if len(results_n) > 1 else results_n.pop()))

print(decision_1(k1, m, k2, p2, n2))


