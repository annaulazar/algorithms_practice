# В Берляндии автомобильные номера состоят из цифр и прописных букв латинского алфавита. Они бывают двух видов:
# · либо автомобильный номер имеет вид буква−цифра−цифра−буква−буква (примеры корректных номеров первого вида:
# R48FA, O00OO, A99OK);
# · либо автомобильный номер имеет вид буква−цифра−буква−буква (примеры корректных номеров второго вида:
# T7RR, A9PQ, O0OO).
# Таким образом, каждый автомобильный номер является строкой либо первого, либо второго вида.
# Вам задана строка из цифр и прописных букв латинского алфавита. Можно ли разделить её пробелами на
# последовательность корректных автомобильных номеров? Иными словами, проверьте, что заданная строка может
# быть образована как последовательность корректных автомобильных номеров, которые записаны подряд без пробелов.
# В случае положительного ответа выведите любое такое разбиение.
# Входные данные
# 6
# R48FAO00OOO0OOA99OKA99OK
# R48FAO00OOO0OOA99OKA99O
# A9PQ
# A9PQA
# A99AAA99AAA99AAA99AA
# AP9QA
# Выходные данные
# R48FA O00OO O0OO A99OK A99OK
# -
# A9PQ
# -
# A99AA A99AA A99AA A99AA
# -

def check_number(number: str) -> bool:
    if len(number) == 4:
        return number[0].isalpha() and number[1].isdigit() and number[2:].isalpha()
    if len(number) == 5:
        return number[0].isalpha() and number[1:3].isdigit() and number[3:].isalpha()
    return False


n = int(input())
for _ in range(n):
    number_string = input().strip()
    index = 0
    numbers = []
    while index < len(number_string):
        if check_number(number_string[index: index + 4]):
            numbers.append(number_string[index: index + 4])
            index += 4
        elif check_number(number_string[index: index + 5]):
            numbers.append(number_string[index: index + 5])
            index += 5
        else:
            print('-')
            break
    else:
        print(*numbers)
