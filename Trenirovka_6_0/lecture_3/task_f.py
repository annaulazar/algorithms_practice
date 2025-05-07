# def right_seq(seq):
#     stack = []
#     for bracket in seq:
#         if bracket in brackets_closed:
#             if not stack:
#                 return False
#             if brackets_closed[bracket] != stack.pop():
#                 return False
#         else:
#             stack.append(bracket)
#     if stack:
#         return False
#     return True


def get_stack(seq, cnt):
    stack = []
    for bracket in seq:
        if bracket in brackets_closed:
            if brackets_closed[bracket] == stack[-1]:
                stack.pop()
                cnt -= 2
        else:
            stack.append(bracket)
    return stack, cnt - len(stack)


def make_min_seq(stack, cnt):
    brackets_open = {'(': ')', '[': ']'}
    suf = []
    while cnt > 0:
        if len(stack) == cnt:
            suf.append(brackets_open[stack.pop()])
            cnt -= 1
        else:
            for bracket in w:
                if bracket in brackets_closed and stack and stack[-1] == brackets_closed[bracket]:
                    suf.append(bracket)
                    stack.pop()
                    cnt -= 1
                    break
                elif bracket in brackets_open:
                    suf.append(bracket)
                    stack.append(bracket)
                    cnt -= 1
                    break
    return suf


n = int(input())
w = input().strip()
s = input().strip()
brackets_closed = {')': '(', ']': '['}
temp_stack, k = get_stack(s, n)
if len(temp_stack) == 0 and k == 0:
    print(s)
else:
    print(s + ''.join(make_min_seq(temp_stack, k)))

