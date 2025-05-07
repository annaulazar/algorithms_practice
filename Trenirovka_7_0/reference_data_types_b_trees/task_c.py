from collections import deque


_queue = deque([])

def push_front(x):
    _queue.appendleft(x)
    return 'ok'

def push_back(x):
    _queue.append(x)
    return 'ok'

def pop_front():
    if _queue:
        return _queue.popleft()
    return 'error'

def pop_back():
    if _queue:
        return _queue.pop()
    return 'error'

def front():
    if _queue:
        return _queue[0]
    return 'error'

def back():
    if _queue:
        return _queue[-1]
    return 'error'

def size():
    return len(_queue)

def my_clear():
    _queue.clear()
    return 'ok'

comands = {'push_front': push_front, 'push_back': push_back, 'pop_front': pop_front,
           'pop_back': pop_back, 'front': front, 'back': back, 'size': size, 'clear': my_clear}
comand_input = input().strip()
while comand_input != 'exit':
    comand_list = comand_input.split()
    comand = comand_list[0]
    if len(comand_list) > 1:
        value = comand_list[1]
        print(comands[comand](value))
    else:
        print(comands[comand]())
    comand_input = input().strip()
print('bye')
