n = int(input())
all_know = set()
m = int(input())
for _ in range(m):
    all_know.add(input().strip())
any_know = all_know.copy()
for _ in range(n - 1):
    m = int(input())
    pupil_now = set()
    for _ in range(m):
        pupil_now.add(input().strip())
    all_know.intersection_update(pupil_now)
    any_know.update(pupil_now)
print(len(all_know))
print(*all_know, sep='\n')
print(len(any_know))
print(*any_know, sep='\n')
