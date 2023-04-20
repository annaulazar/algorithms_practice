with open("input.txt", encoding='utf-8') as file:
    s = file.read()


def right_posl(posl):
    open_list = []
    for x in posl:
        if x == '{':
            open_list.append(x)
        else:
            if len(open_list) == 0:
                return False
            open_list.pop()
    if len(open_list) == 0:
        return True
    return False


sk = ''
for symb in s:
    if symb in '{}':
        sk += symb
if not len(sk) % 2 or abs(sk.count('{') - sk.count('}')) > 1:
    print(-1)
else:
    open = sk.count('{') - sk.count('}')
    for i in range(len(sk)):
        if (sk[i] == '{' and open == 1) or (sk[i] == '}' and open == -1):
            if i == 0 and len(sk) > 1:
                posl = sk[i+1:]
            elif i == len(sk) - 1:
                posl = sk[:i]
            else:
                posl = sk[:i] + sk[i+1:]
            if right_posl(posl):
                index = i
                break
    else:
        print(-1)
        index = -1
    
    if index > -1:
        k = 0
        for j in range(len(s)):
            if s[j] in '{}':
                if k == index:
                    print(j+1)
                    break
                else:
                    k += 1
