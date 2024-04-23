dictionary = set(input().strip().split())
words = list(input().strip().split())
res = []
for word in words:
    for i in range(1, 101):
        pref = word[:i]
        if pref in dictionary:
            res.append(pref)
            break
    else:
        res.append(word)
print(' '.join(res))
