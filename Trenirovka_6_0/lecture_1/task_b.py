# Майки и носки
# Как известно, осенью и зимой светает поздно, и так хочется утром ещё хоть немного поспать, а не идти в школу!
# Некоторые школьники готовы даже одеваться, не открывая глаз, лишь бы отложить момент пробуждения. Вот и Саша решил,
# что майку и носки он вполне может вытащить из шкафа на ощупь с закрытыми глазами и только потом включить свет и одеться.
# В шкафу у Саши есть два ящика. В одном из них лежит A синих и B красных маек, в другом — C синих и D красных пар носков.
# Саша хочет, чтобы и майка, и носки были одного цвета. Он вслепую вытаскивает M маек и N пар носков. В первое же утро
# Саша задумался, какое минимальное суммарное количество предметов одежды (M+N) он должен вытащить, чтобы среди них
# гарантированно оказались майка и носки одного цвета. Какого именно цвета окажутся предметы одежды,
# для Саши совершенно неважно.
# Формат ввода
# На вход программе подаются четыре целых неотрицательных числа A, B, C, D, записанных в отдельных строках:
# A — количество синих маек,
# B — количество красных маек,
# C — количество синих носков,
# D — количество красных носков. Все числа не превосходят 109. Гарантируется, что в шкафу есть одноцветный комплект
# из майки и носков.
# Формат вывода
# Программа должна вывести два числа: количество маек M и количество пар носков N, которые должен взять Саша.
# Необходимо, чтобы среди M маек и N пар носков обязательно нашлась одноцветная пара, при этом сумма M+N должна
# быть минимальной.
# Пример
# Ввод	Вывод
# 6       3 4
# 2
# 7
# 3


a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0:
    if c == 0:
        print(1, 1)
    else:
        print(1, c + 1)
elif b == 0:
    if d == 0:
        print(1, 1)
    else:
        print(1, d + 1)
elif c == 0:
    print(a + 1, 1)
elif d == 0:
    print(b + 1, 1)
else:
    variants = [(a + 1 + c + 1, a + 1, c + 1),
                (b + 1 + d + 1, b + 1, d + 1),
                (max(a, b) + 2, max(a, b) + 1, 1),
                (max(c, d) + 2, 1, max(c, d) + 1)]
    print(*min(variants)[1:])
