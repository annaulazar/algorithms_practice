# 3-правильная очередь
# XY, XZ, YZ - правильные пары
# По набору символов определить можно ли составить правильные пары
import os


# Самый короткий вариант и самый простой - подсчет баланса в двух проходах - вперед и назад
def check_queue(queue) -> bool:
    x, y, z = 0, 0, 0
    for i in range(len(queue)):
        if queue[i] == "X":
            x += 1
        elif queue[i] == "Y":
            y += 1
        elif queue[i] == "Z" and y:
            y -= 1
            z += 1
        elif queue[i] == "Z":
            x -= 1
            # z += 1
        if x < 0:
            return False
    if y > x:
        return False

    # y1, z1 = 0, 0
    # for i in range(len(queue) - 1, -1, -1):
    #     if queue[i] == "X" and y1:
    #         y1 -= 1
    #     elif queue[i] == "X":
    #         z1 -= 1
    #     elif queue[i] == "Y" and z1:
    #         z1 -= 1
    #     elif queue[i] == "Y":
    #         y1 += 1
    #     elif queue[i] == "Z":
    #         z1 += 1
    #     if z1 < 0:
    #         return False
    # if x > y:
    #     return False

    yz = 0
    for i in range(len(queue) - 1, -1, -1):
        if queue[i] == "Z" or queue[i] == "Y":
            yz += 1
        elif queue[i] == "X":
            yz -= 1
        if yz < 0:
            return False
    if x == 0 and y == 0:
        return True
    if x <= y + z * 2:
        x1, y1, z1 = 0, 0, 0
        for j in range(len(queue)):
            if queue[j] == "X":
                x1 += 1
            elif queue[j] == "Y" and x1:
                x1 -= 1
            elif queue[j] == "Y":
                y1 += 1
            elif queue[j] == "Z":
                y1 -= 1
        if y1 > 0:
            return False
        return True

    # xz = 0
    # for i in range(len(queue)):
    #     if queue[i] == "X" or queue[i] == "Z":
    #         xz += 1
    #     elif queue[i] == "Y":
    #         xz -= 1
    # if xz < 0:
    #     return False
    #
    # y, x = 0, 0
    # for i in range(len(queue)):
    #     if queue[i] == "X":
    #         x += 1
    #     elif queue[i] == "Y" and not x:
    #         y += 1
    #     elif queue[i] == "Y":
    #         x -= 1
    #     elif queue[i] == "Z" and y:
    #         y -= 1
    #     elif queue[i] == "Z":
    #         x -= 1
    # if (y > 0) or (x > 0):
    #     return False
    return False


# for _ in range(int(input())):
#     n = int(input())
#     q = input().strip()
#     if n % 2:
#         res = False
#     else:
#         res = check_queue(q)
#     print(['No', 'Yes'][res])

# Проверка файлов с тестовыми данными, что результат совпадает с тестовыми
# path1 = 'test_data'
# path2 = 'result'
# result_files = []
#
# for filename in os.listdir(path2):
#     result_files.append(filename)
#
# i = 0
# for filename in os.listdir(path1):
#     with open(os.path.join(path1, filename), 'r') as file:
#         k = int(file.readline().strip())
#         my_result = []
#         for _ in range(k):
#             n = int(file.readline().strip())
#             q = file.readline().strip()
#             res = check_queue(q)
#             my_result.append(['No', 'Yes'][res])
#     with open(os.path.join(path2, result_files[i]), 'r') as file1:
#         test_result = list(map(str.strip, file1.readlines()))
#     if my_result != test_result:
#         print('Error -', filename)
#     i += 1

# Проверка по найденным файлам где именно выдается ошибка
bad_tests = ['3', '5', '6']
bed_results = ['3.a', '5.a', '6.a']

path1 = 'test_data'
path2 = 'result'

for i, filename in enumerate(bad_tests):
    with open(os.path.join(path2, bed_results[i]), 'r') as f:
        test_result = list(map(str.strip, f.readlines()))
    with open(os.path.join(path1, filename), 'r') as file:
        k = int(file.readline().strip())
        for j in range(k):
            n = int(file.readline().strip())

            q = file.readline().strip()
            res = ['No', 'Yes'][check_queue(q)]
            if test_result[j] != res:
                print(q)
                print(f'My answer: {res}, test answer: {test_result[j]}')

