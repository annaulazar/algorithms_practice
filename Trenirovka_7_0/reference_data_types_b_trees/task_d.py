def push_left(lst, el):
    global head
    if head == -1:
        lst.append([el, None, None])
        head = 0
        return
    lst.append([el, None, head])
    current_ind = len(lst) - 1
    lst[head][1] = current_ind
    head = current_ind


def remove_el_to_head(lst, ind):
    global head
    prev = lst[ind][1]
    next_ = lst[ind][2]
    if prev is not None:
        lst[prev][2] = next_
    if next_ is not None:
        lst[next_][1] = prev
    lst[head][1] = ind
    lst[ind][1] = None
    lst[ind][2] = head
    head = ind


def find_el(lst, k) -> tuple[str, int]:
    next_ind = head
    for i in range(k - 1):
        next_ind = lst[next_ind][2]
    return lst[next_ind][0], next_ind


double_linked_list = []  # Элемент, ссылка на prev, ссылка на next
head = -1
n = int(input())
answer = []
for _ in range(n):
    command = input()
    if command.startswith("Run"):
        program = ' '.join(command.split()[1:])
        answer.append(program)
        push_left(double_linked_list, program)
    else:
        cnt_tab = len(command.split("+")) - 1
        k = cnt_tab % len(double_linked_list) + 1
        program, index = find_el(double_linked_list, k)
        answer.append(program)
        if head != index:
            remove_el_to_head(double_linked_list, index)

print(*answer, sep='\n')
