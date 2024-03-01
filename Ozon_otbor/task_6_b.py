"""
 Рекомендуется использовать быстрый (буферизованный) ввод и вывод
import sys

def fast_input():
	return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x))

a, b = map(int, fast_input().split())
fast_output(a + b)
"""
import sys


def fast_input():
    return sys.stdin.readline().rstrip("\r\n")


for _ in range(int(fast_input())):
    n, m = map(int, fast_input().split())
    table_score = []
    score_list = [0] * 6
    row_scores = [[0] * 6 for _ in range(n)]
    column_scores = [[0] * 6 for _ in range(m)]
    for i in range(n):
        row = list(map(int, list(fast_input())))
        table_score.append(row)
        for j in range(m):
            score_list[row[j]] += 1
            row_scores[i][row[j]] += 1
            column_scores[j][row[j]] += 1
    max_score = 5
    for y in range(5, 0, -1):
        if score_list[y]:
            max_score = min(max_score, y)
            break
    flag = False
    worst = 1
    res_row = 0
    res_column = 0
    for i in range(n):
        for j in range(m):
            for z in range(1, 6):
                temp = score_list[z] - row_scores[i][z] - column_scores[j][z]
                if table_score[i][j] == z:
                    temp += 1
                if temp > 0:
                    if z >= worst:
                        worst = z
                        res_row = i
                        res_column = j
                    break
            if worst == max_score:
                flag = True
                break
        if flag:
            break
    print(res_row + 1, res_column + 1)
