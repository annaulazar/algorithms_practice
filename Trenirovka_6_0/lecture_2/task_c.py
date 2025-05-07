n, r = map(int, input().split())
dist = list(map(int, input().split()))
left = 0
right = 1
res = 0
while left < n-1:
    while right < n-1 and dist[right] - dist[left] <= r:
        right += 1
    if dist[right] - dist[left] > r:
        res += n - right
    left += 1
print(res)
