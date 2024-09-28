name = input().strip()
if len(name) < 8:
    print('NO')
else:
    check = {'digit': 0, 'upper': 0, 'lower': 0}
    english = set('abcdefghijklmnopqrstuvwxyz')
    for letter in name:
        if letter.isdigit():
            check['digit'] += 1
        elif letter.islower() and letter in english:
            check['lower'] += 1
        elif letter.isupper() and letter.lower() in english:
            check['upper'] += 1
    if all([value for value in check.values()]):
        print('YES')
    else:
        print('NO')
