n = int(input())
stack = []
pref_sum = [0] * (n + 1)
for _ in range(n):
    operation = input()
    if operation.startswith('+'):
        num = int(operation[1:])
        stack.append(num)
        ind = len(stack)
        pref_sum[ind] = pref_sum[ind - 1] + num
    elif operation.startswith('-'):
        ind = len(stack)
        num = stack.pop()
        pref_sum[ind] = 0
        print(num)
    elif operation.startswith('?'):
        cnt = int(operation[1:])
        ind = len(stack)
        res = pref_sum[ind] - pref_sum[ind - cnt]
        print(res)
