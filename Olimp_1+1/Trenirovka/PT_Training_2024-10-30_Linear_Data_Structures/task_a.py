def check_seq(seq: list) -> bool:
    stack = []
    if seq[0] != '<' or seq[-1] != '>':
        return False
    if len(seq) <= 2:
        return False
    seq1 = ''.join(seq[1:-1]).split('><')
    for tag in seq1:
        if tag.isalpha():
            stack.append(tag)
        elif tag and tag[0] == '/':
            if stack and stack.pop() == tag[1:]:
                continue
            else:
                return False
        else:
            return False
    if stack:
        return False
    return True


s = list(input())
if s and check_seq(s):
    print('Yes')
else:
    print('No')
