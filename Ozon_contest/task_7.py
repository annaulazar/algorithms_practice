# Пример теста 1
# Входные данные
# 7
# 8
# 7
# 8
# 1,7,1
# 8
# 1-5,1,7-7
# 10
# 1-5
# 10
# 1,2,3,4,5,6,8,9,10
# 3
# 1-2
# 100
# 1-2,3-7,10-20,100
# Выходные данные
# 1-6,8
# 2-6,8
# 6,8
# 6-10
# 7
# 3
# 8-9,21-99

for _ in range(int(input())):
    k = int(input())
    task = input().split(',')
    pages = [0] * (k + 1)
    for elem in task:
        if elem.isdigit():
            page = int(elem)
            pages[page] = 1
        else:
            start_page, end_page = map(int, elem.split('-'))
            for i in range(start_page, end_page + 1):
                pages[i] = 1
    task_new = []
    left, right = 1, 1
    while left <= k or right <= k:
        while left <= k and pages[left] != 0:
            left += 1
        right = left
        while right <= k and pages[right] == 0:
            right += 1
        if right - left == 1:
            task_new.append(str(left))
        elif right - left > 1:
            task_new.append(f"{left}-{right - 1}")
        left = right
    print(','.join(task_new))
