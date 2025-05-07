n, k = map(int, input().split())
s = input().strip()
max_len = 0
rudeness = 0
ab = [0, 0]
left = 0
right = -1
flag_a = False
while left < n and right < (n - 1):
    while right < (n - 1) and rudeness <= k:
        right += 1
        letter = s[right]
        if letter == 'a':
            ab[0] += 1
        elif letter == 'b' and ab[0]:
            rudeness += ab[0]
            ab[1] += 1
    max_len = max(max_len, right - left)
    if right == n - 1 and rudeness <= k:
        max_len = max(max_len, right + 1 - left)
    while left < n and rudeness > k:
        letter_remove = s[left]
        if letter_remove == 'a':
            flag_a = True
            ab[0] -= 1
            rudeness -= ab[1]
            if ab[0] == 0:
                ab[1] = 0
                flag_a = False
        elif letter_remove == 'b' and ab[0] and flag_a:
            ab[1] -= 1
        left += 1
max_len = max(max_len, right - left)
print(max_len)

