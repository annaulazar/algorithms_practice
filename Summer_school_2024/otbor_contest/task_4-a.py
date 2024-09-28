from collections import deque

n, k = map(int, input().strip().split())
costs = list(map(int, input().strip().split()))
by_fish = [0] * n
by_fish[0] = 1
min_cos_queue = deque()
min_cos_queue.append((costs[0], 0))
for i in range(1, n):
    if i >= k and min_cos_queue[0][1] <= i - k:
        min_cos_queue.popleft()
    while min_cos_queue and costs[i] < min_cos_queue[-1][0]:
        min_cos_queue.pop()
    min_cos_queue.append((costs[i], i))

    best_day = min_cos_queue[0][1]
    by_fish[best_day] += 1

res_sum = 0
for i in range(n):
    res_sum += costs[i] * by_fish[i]
print(res_sum)
print(*by_fish)
