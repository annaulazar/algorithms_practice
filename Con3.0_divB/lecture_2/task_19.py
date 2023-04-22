# Куча максимума
# Хипуй
# В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции
# стандартной библиотеки) организовать структуру данных Heap для хранения целых чисел, над
# которой определены следующие операции: a) Insert(k) – добавить в Heap число k ; b) Extract
# достать из Heap наибольшее число (удалив его при этом).
# Формат ввода
# В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд,
# каждая в своей строке. Команда может иметь формат: “0 <число>” или “1”, обозначающий,
# соответственно, операции Insert(<число>) и Extract. Гарантируется, что при выполенении
# команды Extract в структуре находится по крайней мере один элемент.
# Формат вывода
# Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное
# при выполнении команды Extract.
# Пример 1
# Ввод	   Вывод
# 2          10000
# 0 10000
# 1
# Пример 2
# Ввод	  Вывод
# 14        345
# 0 1       4346
# 0 345     2435
# 1         365
# 0 4346    235
# 1         5
# 0 2435    1
# 1
# 0 235
# 0 5
# 0 365
# 1
# 1
# 1
# 1


def push_heap(heap_list, x):
    heap_list.append(x)
    pos = len(heap_list) - 1
    pos_parent = (pos - 1) // 2
    while pos > 0 and heap_list[pos] > heap_list[pos_parent]:
        heap_list[pos], heap_list[pos_parent] = \
            heap_list[pos_parent], heap_list[pos]
        pos = pos_parent
        pos_parent = (pos - 1) // 2


def pop_heap(heap_list):
    ans = heap_list[0]
    heap_list[0] = heap_list[-1]
    pos = 0
    while pos * 2 + 2 < len(heap_list):
        max_son_index = pos * 2 + 1
        if heap_list[pos * 2 + 2] > heap_list[pos * 2 + 1]:
            max_son_index = pos * 2 + 2
        if heap_list[pos] < heap_list[max_son_index]:
            heap_list[pos], heap_list[max_son_index] = \
                heap_list[max_son_index], heap_list[pos]
            pos = max_son_index
        else:
            break
    heap_list.pop()
    return ans

heap = []
n = int(input())
for _ in range(n):
    comands = input().split()
    if comands[0] == '0':
        num = int(comands[1])
        push_heap(heap, num)
    else:
        print(pop_heap(heap))
