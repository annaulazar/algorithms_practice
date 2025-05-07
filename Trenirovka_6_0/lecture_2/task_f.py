# Более крутое решение - посчитать префиксные и суффиксные суммы (или просто по ходу поддерживать)
# и далее в одном проходе результат - сумма произведения каждого элемента на префиксную сумму до него
# и суффиксную сумму после него

# with open ('input48.txt', 'r') as f:
#     n = int(f.readline())
#     a = list(map(int, f.readline().split()))
n = int(input())
a = list(map(int, input().split()))
pref_sum = [0] * (n + 1)
pref_multy_sum = [0] * (n + 1)
pref_sum_multy_sum = [0] * (n + 1)
mode = 1000000007
for i in range(n - 1, -1, -1):
    pref_sum[i] = (pref_sum[i + 1] + a[i]) % mode
    pref_multy_sum[i] = (pref_sum[i + 1] * a[i]) % mode
    pref_sum_multy_sum[i] = (pref_sum_multy_sum[i + 1] + pref_multy_sum[i]) % mode

res = 0
for j in range(n - 2):
    res = (res + a[j] * pref_sum_multy_sum[j + 1]) % mode

print(res % mode)
