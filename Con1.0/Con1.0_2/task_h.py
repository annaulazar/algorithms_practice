# В данном списке из n ≤ 105 целых чисел найдите три числа,произведение которых максимально.
# Решение должно иметь сложность O(n), где n - размер списка.
# Выведите три искомых числа в любом порядке.

from random import randint

nums = [int(x) for x in input().split()]

def my_fast(nums):
    if len(nums) == 3:
        return nums
    else:
        temp = sorted(nums[:5])
        min1, min2 = temp[:2]
        max1, max2, max3 = temp[-3:]
        for num in nums[5:]:
            if num < min1:
                min2 = min1
                min1 = num
            elif min1 <= num < min2:
                min2 = num
            elif num > max3:
                max1 = max2
                max2 = max3
                max3 = num
            elif max2 < num <= max3:
                max1 = max2
                max2 = num
            elif max1 < num <= max2:
                max1 = num
        res = [min1, min2, max1, max2, max3]
        if res[0] * res[1] * res[-1] > res[-3] * res[-2] * res[-1]:
            return [res[0], res[1], res[-1]]
        return [res[-3], res[-2], res[-1]]


print(*my_fast(nums))

def slow(nums):
    n = len(nums)
    res = nums[0] * nums[1] * nums[2]
    res_list = nums[:3]
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                temp = nums[i] * nums[j] * nums[k]
                if temp > res:
                    res = temp
                    res_list = [nums[i], nums[j], nums[k]]
    return res_list

# print(*slow(nums))


# while True:
#     test = []
#     for i in range(10):
#         test.append(randint(-100, 100))
#     fast_res = my_fast(test)
#     slow_res = slow(test)
#     if sorted(fast_res) != sorted(slow_res):
#         print(test, fast_res, slow_res, sep='\n')
#         break

