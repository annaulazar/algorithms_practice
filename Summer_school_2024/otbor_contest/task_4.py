from collections import deque

n, k = map(int, input().strip().split())
costs = list(map(int, input().strip().split()))
by_fish = [0] * n
cnt_fish = min(k, n)
by_fish[0] = cnt_fish
last_by = 0
last_by_cost = costs[0]
min_cos_queue = deque()
min_cos_queue.append((costs[0], 0))
for i in range(1, n):
    if i >= k and min_cos_queue[0][1] <= i - k:
        min_cos_queue.popleft()
    while min_cos_queue and costs[i] < min_cos_queue[-1][0]:
        min_cos_queue.pop()
    min_cos_queue.append((costs[i], i))

    if (min_cos_queue and min_cos_queue[0][0] < last_by_cost) or (i - last_by) >= k:
        remain_days = max(0, (cnt_fish - (i - last_by)))
        by_fish[last_by] -= remain_days

        last_by = min_cos_queue[0][1]
        last_by_cost = min_cos_queue[0][0]
        cnt_fish = min((k - (i - last_by)), n - i)
        by_fish[last_by] = cnt_fish

res_sum = 0
for i in range(n):
    res_sum += costs[i] * by_fish[i]
print(res_sum)
print(*by_fish)
