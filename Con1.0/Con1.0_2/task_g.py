# Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых
# максимально. Выведите эти числа в порядке неубывания.
# Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

nums = [int(x) for x in input().split()]
temp = sorted(nums[:4])
min1, min2 = temp[:2]
max1, max2 = temp[-2:]
for num in nums[4:]:
    if num < min1:
        min2 = min1
        min1 = num
    elif min1 <= num < min2:
        min2 = num
    elif num > max2:
        max1 = max2
        max2 = num
    elif max1 < num <= max2:
        max1 = num
if min1 * min2 > max1 * max2:
    print(min1, min2)
else:
    print(max1, max2)
