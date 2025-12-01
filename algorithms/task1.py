# Найти наименьшее число, которое делится на все числа от 1 до N
def nod(a, b):
    a, b = max(a, b), min(a, b)
    while a % b:
        a, b = b, a % b
    return b


def nok(a, b):
    return (a * b) / nod(a, b)


n = int(input())
answer = 1
for i in range(1, n + 1):
    answer = nok(answer, i)

print(answer)
