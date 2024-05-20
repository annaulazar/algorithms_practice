# 18. Значение арифметического выражения
# Задано числовое выражение. Необходимо вычислить его значение или установить, что оно содержит ошибку.
# В выражении могут встречаться знаки сложения, вычитания, умножения, скобки и пробелы (пробелов внутри
# чисел быть не должно). Приоритет операций стандартный. Все числа в выражении целые и по модулю не
# превосходят 2×109. Также гарантируется, что все промежуточные вычисления также не превосходят 2×10 9.
# Формат ввода
# В первой строке вводится выражение. Его длина не превосходит 100 знаков. После выражения идет переход
# на новую строчку.
# Формат вывода
# Выведите значение этого выражения или слово "WRONG", если значение не определено.
# Пример 1
# Ввод           Вывод
# 1+(2*2 - 3)    2
# Пример 2
# Ввод           Вывод
# 1+a+1          WRONG
# Пример 3
# Ввод           Вывод
# 1 1 + 2        WRONG

def main():
    s = input().strip()
    operators = {'+': 0, '-': 0, '*': 1}
    postf = []
    stack = []
    temp = ''
    f_open = 0
    for i in range(len(s)):
        if s[i] == ' ' and (len(s) - 1) > i > 0 and ((s[i - 1].isdigit() and s[i + 1].isdigit()) or
                                       (s[i - 1] in operators and s[i + 1] in operators)):
            print('WRONG')
            break
        if s[i].isdigit():
            temp += s[i]
        else:
            if temp:
                postf.append(temp)
                temp = ''
            if s[i] == '(':
                stack.append('(')
                f_open += 1
            elif s[i] in operators:
                if i >= 1 and (s[i - 1] in operators or s[i - 1] == '('):
                    print('WRONG')
                    break
                if i == len(s) - 1:
                    print('WRONG')
                    break
                while stack and operators.get(stack[-1], -1) >= operators[s[i]]:
                    postf.append(stack.pop())
                stack.append(s[i])
            elif s[i] == ')' and not f_open:
                print('WRONG')
                break
            elif s[i] == ')' and stack and f_open:
                while stack[-1] != '(':
                    postf.append(stack.pop())
                stack.pop()
                f_open -= 1
            elif s[i] != ' ':
                print('WRONG')
                break
    else:
        if f_open > 0:
            stack = []
            postf = []
        if temp:
            postf.append(temp)
        for _ in range(len(stack)):
            postf.append(stack.pop())
        for sym in postf:
            if sym.isdigit():
                stack.append(int(sym))
            else:
                if stack:
                    arg1 = stack.pop()
                else:
                    break
                if stack:
                    arg2 = stack.pop()
                else:
                    break
                if sym == '-':
                    res = arg2 - arg1
                elif sym == '+':
                    res = arg2 + arg1
                elif sym == '*':
                    res = arg2 * arg1
                else:
                    continue
                stack.append(res)
        if len(stack) == 1:
            print(stack[-1])
        else:
            print('WRONG')


if __name__ == '__main__':
    main()
