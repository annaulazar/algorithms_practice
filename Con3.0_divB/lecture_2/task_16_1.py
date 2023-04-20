from collections import deque


queue = deque([])

def push(x):
    queue.append(x)
    return 'ok'

def my_pop():
    if queue:
        return queue.popleft()
    return 'error'

def front():
    if queue:
        return queue[0]
    return 'error'

def size():
    return len(queue)

def my_clear():
    queue.clear()
    return 'ok'

comands = {'push': push, 'pop': my_pop, 'front': front, 'size': size, 'clear': my_clear}
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
