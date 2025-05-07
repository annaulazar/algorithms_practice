queue = []
start_index = 0

def push(x):
    queue.append(x)
    return 'ok'

def my_pop():
    global start_index
    if len(queue) - start_index > 0:
        start_index += 1
        return queue[start_index - 1]
    return 'error'

def front():
    if len(queue) - start_index > 0:
        return queue[start_index]
    return 'error'

def size():
    return len(queue) - start_index

def my_clear():
    global start_index
    start_index = 0
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
