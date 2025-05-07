a = int(input())
a_bin = bin(a)
res = 0
for i in range(2, len(a_bin)):
    if a_bin[i] == '1':
        res += 1
print(res)
