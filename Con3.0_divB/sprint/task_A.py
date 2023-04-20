n = int(input())

train = []
products = {}

for _ in range(n):
    oper = input().strip().split()
    comand = oper[0]
    if comand == 'add':
        count = int(oper[1])
        prod = oper[-1]
        train.append([count, prod])
        products[prod] = products.get(prod, 0) + count
    elif comand == 'delete':
        count = int(oper[1])
        while count != 0:
            if train[-1][0] <= count:
                cnt, prod = train.pop()
                products[prod] -= cnt
                count -= cnt
            else:
                train[-1][0] -= count
                prod = train[-1][1]
                products[prod] -= count
                count = 0
    elif comand == 'get':
        prod = oper[-1]
        res = products.get(prod, 0)
        print(res)
