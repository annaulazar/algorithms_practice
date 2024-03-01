# k-пила
# Аналитики изучают сезонность цен на некоторые товары. Известно, что они дорожают и дешевеют в зависимости от
# сезона: например, времени года или месяца. По истории цены товара найдите самые длинные отрезки сезонных
# изменений цены.
# file:///C:/Users/Home/AppData/Local/Temp/Rar$EXa33212.45147/k-%D0%BF%D0%B8%D0%BB%D0%B0/Techpoint.htm

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    res = [0] * n
    left, right, middle = 0, 0, 0
    while right < n:
        right += 1
        if a[right] > a[right-1] and middle == left:
            right += 1
        elif a[right] < a[right-1] and middle != left:
            right +=1
