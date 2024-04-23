word1 = input().strip()
word2 = input().strip()
lst1 = [0] * 26
lst2 = [0] * 26
for letter in word1:
    lst1[ord(letter) - 97] += 1
for letter in word2:
    lst2[ord(letter) - 97] += 1
print(['NO', 'YES'][lst1 == lst2])
