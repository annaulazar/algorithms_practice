troom, tcond = (int(i) for i in input().split())
mode = input()
if mode == 'heat':
    print(max(troom, tcond))
elif mode == 'freeze':
    print(min(troom, tcond))
elif mode == 'auto':
    print(tcond)
elif mode == 'fan':
    print(troom)
