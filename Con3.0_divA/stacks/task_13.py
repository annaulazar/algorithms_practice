# Задано логическое выражение. Необходимо вычислить его значение. В выражении могут встречаться знаки ! (отрицание),
# & (логическое «и»), | (логическое «или»), ̂ (XOR — «исключающее ИЛИ», «ровно одно из двух — истина») и скобки.
# Самый высокий приоритет у отрицания, меньше – у &, операции | и ̂ имеют самый низкий приоритет (одинаковый)
# и вычисляются слева направо. Все числа в выражении либо 0, либо 1.
# Формат ввода
# В первой строке вводится выражение. Его длина не превосходит 100 знаков. После выражения идет переход
# на новую строчку.
# Формат вывода
# Выведите значение этого выражения (0 или 1)
# Пример
# Ввод	   Вывод
# 1|(0&0^1)  1


s = list(input())
operators = {'|': 0, '^': 0, '&': 1, '!': 2}
postf = []
stack = []
for i in range(len(s)):
    if s[i].isdigit():
        postf.append(s[i])
    elif s[i] in operators:
        while stack and operators.get(stack[-1], -1) >= operators[s[i]]:
            postf.append(stack.pop())
        stack.append(s[i])
    elif s[i] == '(':
        stack.append('(')
    elif s[i] == ')':
        while stack[-1] != '(':
            postf.append(stack.pop())
        stack.pop()

for _ in range(len(stack)):
    postf.append(stack.pop())

for sym in postf:
    if sym.isdigit():
        stack.append(int(sym))
    elif sym != '!':
        arg1 = stack.pop()
        arg2 = stack.pop()
        if sym == '|':
            res = arg2 | arg1
        elif sym == '&':
            res = arg2 & arg1
        elif sym == '^':
            res = arg2 ^ arg1
        stack.append(res)
    elif sym == '!':
        arg = stack.pop()
        res = 1 - arg
        stack.append(res)
print(stack[-1])
