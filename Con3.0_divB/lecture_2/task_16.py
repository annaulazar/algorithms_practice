# Реализация на обычнм массиве со сдвиглм начального элемента
# Очередь с защитой от ошибок
# Научитесь пользоваться стандартной структурой данных queue для целых чисел. Напишите программу,
# содержащую описание очереди и моделирующую работу очереди, реализовав все указанные здесь методы.
# Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную
# операцию. После выполнения каждой команды программа должна вывести одну строчку.
# Возможные команды для программы:
# push n
# Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.
# pop
# Удалить из очереди первый элемент. Программа должна вывести его значение.
# front
# Программа должна вывести значение первого элемента, не удаляя его из очереди.
# size
# Программа должна вывести количество элементов в очереди.
# clear
# Программа должна очистить очередь и вывести ok.
# exit
# Программа должна вывести bye и завершить работу.
# Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя
# бы один элемент. Если во входных данных встречается операция front или pop, и при этом очередь
# пуста, то программа должна вместо числового значения вывести строку error.
# Формат ввода
# Вводятся команды управления очередью, по одной на строке
# Формат вывода
# Требуется вывести протокол работы очереди, по одному сообщению на строке

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
