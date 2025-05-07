num = int(input())
z = len(bin(num)) - 2
res = num
last_bit = int(bin(num)[-1])
new_num = (num >> 1) ^ (last_bit << (z - 1))
while new_num != num:
    res = max(res, new_num)
    last_bit = int(bin(new_num)[-1])
    new_num = (new_num >> 1) ^ (last_bit << (z - 1))
print(res)
