n = int(input())
a = list(map(int, input().split()))
a.sort()
right = n // 2
left = right - 1
answer = []
if n % 2:
    answer.append(a[right])
    right += 1
while left >= 0 and right < n:
    answer.append(a[left])
    answer.append(a[right])
    left -= 1
    right += 1
print(*answer)
