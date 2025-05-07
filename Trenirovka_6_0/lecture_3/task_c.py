from collections import deque


n, k = map(int, input().split())
nums = list(map(int, input().split()))
que = deque()
for i in range(k):
    while que and nums[i] < que[-1][0]:
        que.pop()
    que.append((nums[i], i))
print(que[0][0])
for j in range(k, n):
    if que[0][1] < j - k + 1:
        que.popleft()
    while que and nums[j] < que[-1][0]:
        que.pop()
    que.append((nums[j], j))
    print(que[0][0])
