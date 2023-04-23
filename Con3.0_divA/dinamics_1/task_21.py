# Дано натуральное число N. Необходимо представить его в виде суммы точных кубов, содержащей наименьшее число слагаемых.
# Программа должна вывести это число слагаемых.
# Формат ввода
# Программа получает на вход натуральное число N, не превосходящее 106
# Формат вывода
# Программа должна вывести единственное натуральное число
# Пример
# Ввод	Вывод
# 9       2


n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    min_step = n
    k = 1
    while k**3 <= i:
        tek = dp[i - k**3]
        if tek < min_step:
            min_step = tek
        k += 1
    dp[i] = min_step + 1
print(dp[n])