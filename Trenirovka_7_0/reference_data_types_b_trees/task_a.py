s = input()
stack = []
while s != 'exit':
    s = s.split()
    comand = s[0]
    if len(s) > 1:
        value = int(s[1])
    if comand == 'push':
        stack.append(value)
        print('ok')
    elif comand == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print('error')
    elif comand == 'back':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print('error')
    elif comand == 'size':
        print(len(stack))
    elif comand == 'clear':
        stack.clear()
        print('ok')
    s = input()
print('bye')
