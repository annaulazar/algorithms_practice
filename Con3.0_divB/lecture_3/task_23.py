n = int(input())
dp = [0] * (n + 1)
best_pos = [-1] * (n + 1)
for i in range(2, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        if dp[i // 3] <= dp[i // 2] and dp[i // 3] <= dp[i - 1]:
            best_pos[i] = i // 3
            dp[i] = dp[i // 3] + 1
        elif dp[i // 2] <= dp[i // 3] and dp[i // 2] <= dp[i - 1]:
            best_pos[i] = i // 2
            dp[i] = dp[i // 2] + 1
        else:
            best_pos[i] = i - 1
            dp[i] = dp[i - 1] + 1
    elif i % 2 == 0:
        if dp[i // 2] <= dp[i - 1]:
            best_pos[i] = i // 2
            dp[i] = dp[i // 2] + 1
        else:
            best_pos[i] = i - 1
            dp[i] = dp[i - 1] + 1
    elif i % 3 == 0:
        if dp[i // 3] <= dp[i - 1]:
            best_pos[i] = i // 3
            dp[i] = dp[i // 3] + 1
        else:
            best_pos[i] = i - 1
            dp[i] = dp[i - 1] + 1
    else:
        best_pos[i] = i - 1
        dp[i] = dp[i - 1] + 1
ans = [n]
k = n
while best_pos[k] != -1:
    temp = best_pos[k]
    ans.append(temp)
    k = temp
print(len(ans) - 1)
print(*ans[::-1])
