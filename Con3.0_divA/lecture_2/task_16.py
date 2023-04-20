from collections import deque

n, k = map(int, input().split())
nums = [int(x) for x in input().split()]
deque_ = deque()
for i in range(k):
    deque_.append(nums[i])
cur_min = min(deque_)
print(cur_min)
for j in range(1, n - k + 1):
    deque_.popleft()
    deque_.append(nums[j + k - 1])
    if deque_[-1] < cur_min:
        cur_min = deque_[-1]
    elif nums[j - 1] == cur_min:
        cur_min = min(deque_)
    print(cur_min)
