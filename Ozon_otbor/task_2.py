for _ in range(int(input())):
    n, p = map(int, input().split())
    res = 0
    for _ in range(n):
        cost = int(input())
        comis = cost * p / 100
        res += (comis - int(comis))
    print(f"{res:.2f}")
