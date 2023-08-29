# Найти наименьшее число, которое делится на все числа от 1 до N

n = int(input())
num = n*(n-1)
try:
    while True:
        for i in range(1, n + 1):
            if num % i:
                break
        else:
            print(num)
            break
        num *= n*(n-1)
except KeyboardInterrupt:
    print(num)
