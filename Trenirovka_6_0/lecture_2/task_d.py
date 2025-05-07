n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
right = 0
max_dist = 0
for left in range(n):
    while right < n and a[right] - a[left] <= k:
        right += 1
    max_dist = max(max_dist, right - left)
print(max_dist)
