from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))
stack = deque()
for i in range(k):
    if not stack or stack[-1][0] <= nums[i]:
        stack.append((nums[i], i))
    else:
        while stack and stack[-1][0] > nums[i]:
            stack.pop()
        stack.append((nums[i], i))
print(stack[0][0], end=' ')
for j in range(1, n - k + 1):
    if stack[0][1] < j:
        stack.popleft()
    if not stack or stack[-1][0] <= nums[j + k - 1]:
        stack.append((nums[j + k - 1], j + k - 1))
    else:
        while stack and stack[-1][0] > nums[j + k - 1]:
            stack.pop()
        stack.append((nums[j + k - 1], j + k - 1))
    print(stack[0][0], end=' ')
