n = int(input())
town_costs = [(int(x), i) for i, x in enumerate(input().split())]
answer = [-1] * n
stack = []
for t in town_costs:
    while stack and stack[-1][0] > t[0]:
        answer[stack[-1][1]] = t[1]
        stack.pop()
    stack.append(t)
print(*answer)
