n, m = map(int, input().split())
words = {}
s = input().strip()
for i in range(m):
    word = input().strip()
    if word not in words:
        words[word] = set()
    words[word].add(i)

res = []
k = n // m
for j in range(0, n, k):
    part = s[j:j + k]
    res.append(words[part].pop() + 1)

print(*res)
