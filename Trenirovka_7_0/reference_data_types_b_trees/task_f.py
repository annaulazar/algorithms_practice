from collections import deque

n = int(input())
piggy_bank = {}
for i in range(1, n + 1):
    piggy = int(input())
    if piggy not in piggy_bank:
        piggy_bank[piggy] = set()
    piggy_bank[piggy].add(i)

keys = sorted(piggy_bank.keys(), key=lambda x: -len(piggy_bank[x]))
for key in keys:
    if piggy_bank[key]:
        que = deque()
        for el in piggy_bank[key]:
            que.append(el)
        while que:
            current = que.popleft()
            if piggy_bank.get(current, None):
                for el2 in piggy_bank[current]:
                    if el2 not in piggy_bank[key] and el2 != key:
                        que.append(el2)
                        piggy_bank[key].add(el2)
                if current != key:
                    piggy_bank[current] = set()

answer = 0
for key in piggy_bank:
    if piggy_bank[key]:
        answer += 1
print(answer)
