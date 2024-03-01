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


def check_for_rows(n, m, table, scores: list):
    worst = 1
    res_row = 0
    res_column = 0
    for i in range(n):
        new_scores = scores.copy()
        for score in table[i]:
            new_scores[score] -= 1
        for j in range(m):
            temp_scores = new_scores.copy()
            for k in range(n):
                if k != i:
                    temp_scores[table[k][j]] -= 1
            for z in range(1, 6):
                if temp_scores[z]:
                    if z >= worst:
                        worst = z
                        res_row = i
                        res_column = j
                    break
    return res_row, res_column


def check_for_columns(n, m, table, scores: list):
    worst = 1
    res_row = 0
    res_column = 0
    for j in range(m):
        new_scores = scores.copy()
        for x in range(n):
            new_scores[table[x][j]] -= 1
        for i in range(n):
            temp_scores = new_scores.copy()
            temp = table[i][:j] + table[i][j + 1:]
            for temp_score in temp:
                temp_scores[temp_score] -= 1
            for z in range(1, 6):
                if temp_scores[z]:
                    if z >= worst:
                        worst = z
                        res_row = i
                        res_column = j
                    break
    return res_row, res_column


for _ in range(int(fast_input())):
    n, m = map(int, fast_input().split())
    table_score = []
    score_list = [0] * 6
    for i in range(n):
        row = list(map(int, list(fast_input())))
        table_score.append(row)
        for j in range(m):
            score_list[row[j]] += 1
    if n > m:
        row, column = check_for_columns(n, m, table_score, score_list)
    else:
        row, column = check_for_rows(n, m, table_score, score_list)

    print(row + 1, column + 1)
