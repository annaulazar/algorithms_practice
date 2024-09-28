sample = input().strip()
log = input().strip()
result = []
cursor = 0
ind = 0
while ind < len(log):
    if log[ind].isalpha():
        result.insert(cursor, log[ind])
        ind += 1
        cursor += 1
    else:
        if log[ind + 1] == 'l':
            cursor = max(0, cursor - 1)
            ind += 6
        elif log[ind + 1] == 'r':
            cursor = min(len(result), cursor + 1)
            ind += 7
        elif log[ind + 1] == 'b':
            if cursor > 0:
                result.pop(cursor - 1)
                cursor -= 1
            ind += 8
        elif log[ind + 1] == 'd':
            if cursor < len(result):
                result.pop(cursor)
            ind += 8
if sample == ''.join(result):
    print('Yes')
else:
    print('No')
