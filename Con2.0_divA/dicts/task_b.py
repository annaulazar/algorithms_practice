n, m = map(int, input().split())
letters = {}
for _ in range(n):
    row = input().strip()
    for symbol in row:
        letters[symbol] = letters.get(symbol, 0) + 1
for _ in range(m):
    word = input().strip()
    for letter in word:
        letters[letter] -= 1
print(''.join([key * value for (key, value) in letters.items() if value > 0]))
