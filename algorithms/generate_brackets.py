# Генерация правильных скобочных последовательностей

def generate_brackets(current: str, opened: int, closed: int, n):
    if len(current) == 2 * n:
        print(current)
        return
    if opened < n:
        generate_brackets(current + '(', opened + 1, closed, n)
    if closed < opened:
        generate_brackets(current + ')', opened, closed + 1, n)


# Для уменьшения рекурсий
def gen_brack(current, opened, closed, n):
    if opened < n:
        for i in range(n, max(opened, closed + 1) - 1, -1):
            gen_brack(current + (i - opened) * '(' + ')', i, closed + 1, n)
    else:
        print(current + (n - closed) * ')')


n = int(input())
# generate_brackets('', 0, 0, n)
gen_brack('', 0, 0, n)
