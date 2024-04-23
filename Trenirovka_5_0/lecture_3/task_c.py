n = int(input())
nums = list(map(int, input().split()))
sorted_nums = [0] * 200001
for number in nums:
    sorted_nums[number] += 1
res = 0
for i in range(1, 200001):
    temp = sorted_nums[i] + sorted_nums[i - 1]
    res = max(res, temp)
print(n - res)
