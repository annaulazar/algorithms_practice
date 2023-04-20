n = int(input())

courier1 = courier2 = 0

for i in range(n):
    a, b = map(int, input().split())
    courier1_svob = courier1 + a
    courier2_svob = courier2 + b

    if courier1_svob <= courier2_svob:
        print("1", end=' ')
        courier1 += a
    else:
        print("2", end=' ')
        courier2 += b
