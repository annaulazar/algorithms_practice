s = input()
n = len(s)
n_words = int(input())
words = set()
for _ in range(n_words):
    word = input().strip()
    words.add(word)
dp = [0] * (n + 1)
prev = [0] * (n + 1)
dp[0] = 1
for i in range(n):
    if dp[i] == 0:
        continue
    for j in range(i, n):
        temp = s[i:j + 1]
        if temp in words and dp[j + 1] == 0:
            dp[j + 1] = 1
            prev[j + 1] = j + 2 - len(temp)

res = []
x = n
while prev[x] != 0:
    res_word = s[prev[x] - 1:x]
    res.append(res_word)
    x = prev[x] - 1

print(' '.join(res[::-1]))
