def right_seq(seq):
    brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for bracket in seq:
        if bracket in brackets:
            if not stack:
                return False
            if brackets[bracket] != stack.pop():
                return False
        else:
            stack.append(bracket)
    if stack:
        return False
    return True


s = input()
print(('no', 'yes')[right_seq(s)])
