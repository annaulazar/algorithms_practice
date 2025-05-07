# вариант для ограничения в задаче, что |vi - v(i+1)|<=10, структура двусвязный список с поддержкой последнего элемента, над которым было действие и соответсвенно идем в одну или другую сторону по ссылкам не больше 10 раз
def remove_el(lst, ind):
    prev = lst[ind][1]
    next_ = lst[ind][2]
    lst[prev][2] = next_
    lst[next_][1] = prev
    lst[ind] = [0, None, None]


def pop_left(lst, ind):
    global head
    next_ = lst[head][2]
    lst[next_][1] = None
    head = next_
    lst[ind] = [0, None, None]


def pop_right(lst, ind):
    global tail
    prev = lst[tail][1]
    lst[prev][2] = None
    tail = prev
    lst[ind] = [0, None, None]


def insert_el(lst, ind):
    insert_ind = len(lst) - 1
    prev = lst[ind][1]
    if prev is not None:
        lst[prev][2] = insert_ind
        lst[insert_ind][1] = prev
        lst[insert_ind][2] = ind
        lst[ind][1] = insert_ind


def push_right(lst):
    global tail
    insert_ind = len(lst) - 1
    lst[tail][2] = insert_ind
    lst[insert_ind][1] = tail
    tail = insert_ind


def find_el(lst, cur_ind, cur_order, number):
    if number > cur_order:
        for i in range(number - cur_order):
            cur_ind = lst[cur_ind][2]
    elif number < cur_order:
        for i in range(cur_order - number):
            cur_ind = lst[cur_ind][1]
    return cur_ind


def bankrot(lst, ind):
    global result
    global current_index
    global current_order
    global cnt
    cnt -= 1
    value = lst[ind][0]
    result -= value ** 2
    prev = lst[ind][1]
    next_ = lst[ind][2]
    if prev is not None:
        result -= lst[prev][0] ** 2
    if next_ is not None:
        result -= lst[next_][0] ** 2
    if prev is None:
        current_index = next_
        lst[next_][0] += value
        result += lst[next_][0] ** 2
        pop_left(lst, ind)
    elif next_ is None:
        current_index = prev
        current_order -= 1
        lst[prev][0] += value
        result += lst[prev][0] ** 2
        pop_right(lst, ind)
    else:
        current_index = next_
        lst[prev][0] += value // 2
        lst[next_][0] += (value - value // 2)
        result += lst[next_][0] ** 2
        result += lst[prev][0] ** 2
        remove_el(lst, ind)


def devision(lst, ind):
    global result
    global cnt
    cnt += 1
    value = lst[ind][0]
    result -= value ** 2
    value1 = value // 2
    value2 = value - value1
    result += (value1 ** 2 + value2 ** 2)
    lst[ind][0] = value1
    lst.append([value2, None, None])
    if ind == tail:
        push_right(lst)
    else:
        insert_el(lst, lst[ind][2])

n = int(input())
cnt = n
river_lengths = list(map(int, input().split()))
result = sum(x ** 2 for x in river_lengths)
company_list = [[river_lengths[i], i - 1, i + 1] for i in range(n)]
company_list[0][1] = None
company_list[n - 1][2] = None
head = 0
tail = n - 1
k = int(input())
current_index = -1 # индекс в массиве и порядковый номер элемнта текущего
current_order = 0
print(result)
for i in range(k):
    com, num = map(int, input().split())
    if i == 0:
        current_index, current_order = num - 1, num
    else:
        current_index = find_el(company_list, current_index, current_order, num)
        current_order = num
    if com == 1:
        bankrot(company_list, current_index)

    else:
        devision(company_list, current_index)
    print(result)
