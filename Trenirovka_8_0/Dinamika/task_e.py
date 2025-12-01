from collections import deque


n, k = map(int, input().split())
a = list(map(int, input().split()))

pref_sum = [0] * (n + 1)
for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + a[i - 1]

dp = [0] * n
prev = [-1] * n
# Для минимума в окне
que = deque()

for j in range(k):
    while que and a[j] < que[-1][0]:
        que.pop()
    que.append((a[j], j))
dp[k - 1] = (pref_sum[k] - pref_sum[0]) * que[0][0]
prev[k - 1] = 0
for j in range(k, n):
    if que[0][1] < j - k + 1:
        que.popleft()
    while que and a[j] < que[-1][0]:
        que.pop()
    que.append((a[j], j))
    taken = (pref_sum[j + 1] - pref_sum[j + 1 - k]) * que[0][0]
    if dp[j - k] + taken > dp[j - 1]:
        dp[j] = dp[j - k] + taken
        prev[j] = j - k + 1
    else:
        dp[j] = dp[j - 1]

res = []
x = 0
max_ref = dp[0]
for z in range(n):
    if dp[z] > max_ref:
        max_ref = dp[z]
        x = z

while x >= 0:
    res.append(prev[x] + 1)
    x = prev[x] - 1
    while prev[x] == -1:
        x -= 1

print(len(res))
print(*res[::-1])
