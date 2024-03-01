# В офисе стоит кондиционер, на котором можно установить температуру от 15 до 30 градусов.
# В офис по очереди приходят n сотрудников. i-й из них желает температуру не больше или не меньше ai.
# После прихода каждого сотрудника определите, можно ли выставить температуру, которая удовлетворит всех в офисе.
# Входные данные
# 4
# 1
# >= 30
# 6
# >= 18
# <= 23
# >= 20
# <= 27
# <= 21
# >= 28
# 3
# <= 25
# >= 20
# >= 25
# 3
# <= 15
# >= 30
# <= 24
# Выходные данные
# 30
#
# 18
# 18
# 20
# 20
# 20
# -1
#
# 15
# 20
# 25
#
# 15
# -1
# -1

n = int(input())
j = 1
for _ in range(n):
    k = int(input())
    span = [15, 30]
    flag_stop = False
    for i in range(k):
        s = input().strip()
        if flag_stop:
            print(-1)
            continue
        temperature = int(s[-2:])
        if s.startswith('>'):
            span[0] = max(span[0], temperature)
        elif s.startswith('<'):
            span[1] = min(span[1], temperature)
        if span[0] <= span[1]:
            print(span[0])
        else:
            flag_stop = True
            print(-1)
    print()
