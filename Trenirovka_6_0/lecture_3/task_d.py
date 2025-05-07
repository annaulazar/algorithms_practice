post_record = input().split()
stack = []
for el in post_record:
    if el.isdigit():
        stack.append(int(el))
    else:
        arg1 = stack.pop()
        arg2 = stack.pop()
        if el == '-':
            res = arg2 - arg1
        elif el == '+':
            res = arg2 + arg1
        elif el == '*':
            res = arg2 * arg1
        else:
            continue
        stack.append(res)
print(stack[-1])
