n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x = list(map(int, input().split()))
pref_cnt = [0] * n
left = 0
temp = 0
for right in range(1, n):
    if a[right] > a[right - 1]:
        pref_cnt[right] = right - left
    elif a[right] < a[right - 1]:
        temp = 0
        left = right
    elif a[right] == a[right - 1]:
        temp += 1
        while temp > k:
            left += 1
            if a[left] == a[left - 1]:
                temp -= 1
        pref_cnt[right] = right - left
answer = [0] * m
for i in range(m):
    xi = x[i]
    stop_pos = xi - pref_cnt[xi - 1]
    answer[i] = stop_pos
print(*answer)
