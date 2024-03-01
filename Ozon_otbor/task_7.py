n = int(input())
employers = set()
for _ in range(n):
    parol = input().strip()
    employers.add(hash(parol))
    for i in range(len(parol) - 1):
        new_parol = parol[:i] + parol[i + 1] + parol[i] + parol[i + 2:]
        employers.add(hash(new_parol))
m = int(input())
for _ in range(m):
    new_employer_parol = input().strip()
    if hash(new_employer_parol) in employers:
        print('1')
    else:
        print('0')
