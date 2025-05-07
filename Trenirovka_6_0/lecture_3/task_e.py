# Решение не отлавливает все некорректные выражения, например '2(3+4*)' выдает 14
# На разборе было решение, которое скорее всего отлавливает: добавляем 0 к унарному минусу (в начале строки и после скобок),
# добавляем пробелы вокруг операторов и скобок, нарезаем все по пробелам и проходим по элементам, складывая в постфиксную
# запись. При этом поддерживаем последний тип элемента (число, скобка или оператор), и отлавливаем случаи, когда некорректные
# типы идут рядом (оператор после оператора, два числа, скобка сразу после оператора и т.п.)
def make_postfix(seq: str) -> list | None:
    operators = {'+': 0, '-': 0, '*': 1}
    postfix = []
    stack = []
    temp = ''
    f_open = 0
    for i in range(len(seq)):
        if seq[i] == ' ' and ((seq[i - 1].isdigit() and seq[i + 1].isdigit()) or
                            (seq[i - 1] in operators and seq[i + 1] in operators)):
            return None
        if seq[i].isdigit():
            temp += seq[i]
        else:
            if temp:
                postfix.append(temp)
                temp = ''
            if seq[i] == '(':
                stack.append('(')
                f_open += 1
            elif seq[i] in operators:
                while stack and operators.get(stack[-1], -1) >= operators[seq[i]]:
                    postfix.append(stack.pop())
                stack.append(seq[i])
            elif seq[i] == ')' and not f_open:
                return None
            elif seq[i] == ')' and f_open:
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
                f_open -= 1
            elif seq[i] != ' ':
                return None
    if temp:
        postfix.append(temp)
    for _ in range(len(stack)):
        postfix.append(stack.pop())
    if not postfix or f_open > 0:
        return None
    return postfix


def calculate_postfix(postfix: list) -> int | None:
    stack = []
    for el in postfix:
        if el.isdigit():
            stack.append(int(el))
        else:
            if len(stack) < 2:
                return None
            arg1 = stack.pop()
            arg2 = stack.pop()
            if el == '-':
                res = arg2 - arg1
            elif el == '+':
                res = arg2 + arg1
            elif el == '*':
                res = arg2 * arg1
            else:
                continue
            stack.append(res)
    if len(stack) > 1 or len(stack) == 0:
        return None
    return stack[-1]


s = input().strip()
postf = make_postfix(s)
if postf is None:
    print('WRONG')
else:
    res = calculate_postfix(postf)
    if res is None:
        print('WRONG')
    else:
        print(res)
