def nod(a, b):
    a, b = max(a, b), min(a, b)
    while a % b:
        a, b = b, a % b
    return b


def nok(a, b):
    return int((a * b) / nod(a, b))


print(nod(6,3))
print(nok(75, 60))