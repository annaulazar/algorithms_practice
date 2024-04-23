n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums_dict = {}
for i in range(min(k + 1, n)):
    if nums[i] not in nums_dict:
        nums_dict[nums[i]] = 1
    else:
        print('YES')
        break
else:
    for j in range(k + 1, n):
        nums_dict[nums[j - k - 1]] -= 1
        if nums[j] in nums_dict and nums_dict[nums[j]] >= 1:
            print('YES')
            break
        else:
            nums_dict[nums[j]] = 1
    else:
        print('NO')
