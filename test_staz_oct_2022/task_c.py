def comparsion(word1, word2):
    dif = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            dif += 1
    if dif > 1:
        dif = 0
    return dif


n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())
def slow():
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans += comparsion(words[i], words[j])
    print(ans)

slow()
