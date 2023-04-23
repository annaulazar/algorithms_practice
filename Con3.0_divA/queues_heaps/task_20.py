# Петя, которому три года, очень любит играть с машинками. Всего у Пети N различных машинок, которые хранятся
# на полке шкафа так высоко, что он сам не может до них дотянуться. Одновременно на полу комнаты может
# находиться не более K машинок. Петя играет с одной из машинок на полу и если он хочет поиграть с другой
# машинкой, которая также находится на полу, то дотягивается до нее сам. Если же машинка находится на
# полке, то он обращается за помощью к маме. Мама может достать для Пети машинку с полки и одновременно
# с этим поставить на полку любую машинку с пола. Мама очень хорошо знает своего ребенка и может
# предугадать последовательность, в которой Петя захочет играть с машинками. При этом, чтобы не мешать
# Петиной игре, она хочет совершить как можно меньше операций по подъему машинки с пола, каждый раз
# правильно выбирая машинку, которую следует убрать на полку. Ваша задача состоит в том, чтобы определить
# минимальное количество операций. Перед тем, как Петя начал играть, все машинки стоят на полке.
# Формат ввода
# В первой строке содержаться три числа N, K и P (1≤K≤N≤100000, 1≤P≤500000). В следующих P строках
# записаны номера машинок в том порядке, в котором Петя захочет играть с ними.
# Формат вывода
# Выведите единственное число: минимальное количество операций, которое надо совершить Петиной маме.
# Пример
# Ввод	Вывод
# 3 2 7   4
# 1
# 2
# 3
# 1
# 3
# 1
# 2

def push_heap(heap_list, heap_dict, x):
    heap_list.append(x)
    pos = len(heap_list) - 1
    heap_dict[x[0]] = pos
    pos_parent = (pos - 1) // 2
    while pos > 0 and heap_list[pos][1] > heap_list[pos_parent][1]:
        heap_list[pos], heap_list[pos_parent] = \
            heap_list[pos_parent], heap_list[pos]
        heap_dict[heap_list[pos][0]] = pos
        heap_dict[heap_list[pos_parent][0]] = pos_parent
        pos = pos_parent
        pos_parent = (pos - 1) // 2


def pop_heap(heap_list, heap_dict):
    ans = heap_list[0]
    heap_list[0] = heap_list[-1]
    pos = 0
    while pos * 2 + 2 < len(heap_list):
        max_son_index = pos * 2 + 1
        if heap_list[pos * 2 + 2][1] > heap_list[pos * 2 + 1][1]:
            max_son_index = pos * 2 + 2
        if heap_list[pos][1] < heap_list[max_son_index][1]:
            heap_list[pos], heap_list[max_son_index] = \
                heap_list[max_son_index], heap_list[pos]
            heap_dict[heap_list[pos][0]] = pos
            heap_dict[heap_list[max_son_index][0]] = max_son_index
            pos = max_son_index
        else:
            break
    heap_list.pop()
    del cars_heap_pos[ans[0]]
    return ans


def change_heap(heap_list, heap_dict, x):
    pos = heap_dict[x[0]]
    heap_list[pos][1] = x[1]
    pos_parent = (pos - 1) // 2
    while pos > 0 and heap_list[pos][1] > heap_list[pos_parent][1]:
        heap_list[pos], heap_list[pos_parent] = \
            heap_list[pos_parent], heap_list[pos]
        heap_dict[heap_list[pos][0]] = pos
        heap_dict[heap_list[pos_parent][0]] = pos_parent
        pos = pos_parent
        pos_parent = (pos - 1) // 2


n, k, p = map(int, input().split())
cars = [[int(input()), p] for _ in range(p)]
cars_dict = {}
for i in range(p-1, -1, -1):
    if cars[i][0] in cars_dict:
        cars[i][1] = cars_dict[cars[i][0]]
    cars_dict[cars[i][0]] = i
del cars_dict
answer = 0
cars_heap = []
cars_heap_pos = {}
cars_set = set()
j = 0
while len(cars_set) < k:
    if cars[j][0] not in cars_set:
        push_heap(cars_heap, cars_heap_pos, cars[j])
        cars_set.add(cars[j][0])
        answer += 1
    else:
        change_heap(cars_heap, cars_heap_pos, cars[j])
    j += 1
for i in range(j, p):
    if cars[i][0] not in cars_set:
        temp = pop_heap(cars_heap, cars_heap_pos)[0]
        push_heap(cars_heap, cars_heap_pos, cars[i])
        answer += 1
        cars_set.remove(temp)
        cars_set.add(cars[i][0])
    else:
        change_heap(cars_heap, cars_heap_pos, cars[i])

print(answer)
