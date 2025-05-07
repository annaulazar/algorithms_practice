from collections import deque


def get_travel_order(a, b):
    a, b = min(a, b), max(a, b)
    if a == 1 and b == 3:
        order = [(1, 3), (2, 4)]
    elif a == 2 and b == 4:
        order = [(2, 4), (1, 3)]
    elif a == 1 and b == 2:
        order = [1, 2, 3, 4]
    elif a == 1 and b == 4:
        order = [4, 1, 2, 3]
    elif a == 2 and b == 3:
        order = [2, 3, 4, 1]
    elif a == 3 and b == 4:
        order = [3, 4, 1, 2]
    return order


n = int(input())
a, b = map(int, input().split())
rovers = []
for i in range(n):
    d, t = map(int, input().split())
    rovers.append([t, d, i])
rovers.sort()

ques = {1: deque(), 2: deque(), 3: deque(), 4: deque()}
for rover in rovers:
    t, d, i = rover
    ques[d].append([t, i])

travel_order = get_travel_order(a, b)
answer = [0] * n
minute = 1
while ques[1] or ques[2] or ques[3] or ques[4]:
    flag_priority = False
    for priority in travel_order:
        if isinstance(priority, tuple):
            for number in priority:
                if ques[number] and ques[number][0][0] <= minute:
                    answer[ques[number][0][1]] = minute
                    ques[number].popleft()
                    flag_priority = True
        else:
            if ques[priority] and ques[priority][0][0] <= minute:
                answer[ques[priority][0][1]] = minute
                ques[priority].popleft()
                flag_priority = True
        if flag_priority:
            break
    minute += 1

for el in answer:
    print(el)
