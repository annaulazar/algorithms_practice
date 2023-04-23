# Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания Российской Федерации”
# определяет следующий алгоритм пропорционального распределения мест в парламенте.
# Необходимо распределить 450 мест между партиями, участвовавших в выборах. Сначала подсчитывается сумма
# голосов избирателей, поданных за каждую партию и подсчитывается сумма голосов, поданных за все партии. Эта
# сумма делится на 450, получается величина, называемая “первое избирательное частное” (смысл первого
# избирательного частного - это количество голосов избирателей, которое необходимо набрать для получения
# одного места в парламенте).
# Далее каждая партия получает столько мест в парламенте, чему равна целая часть от деления числа голосов
# за данную партию на первое избирательное частное.
# Если после первого раунда распределения мест сумма количества мест, отданных партиям, меньше 450, то
# оставшиеся места передаются по одному партиям, в порядке убывания дробной части частного от деления числа
# голосов за данную партию на первое избирательное частное. Если же для двух партий эти дробные части равны,
# то преимущество отдается той партии, которая получила большее число голосов.
# Формат ввода
# На вход программе подается список партий, участвовавших в выборах. Каждая строка входного файла содержит название
# партии (строка, возможно, содержащая пробелы), затем, через пробел, количество голосов, полученных
# данной партией – число, не превосходящее 108.
# Формат вывода
# Программа должна вывести названия всех партий и количество голосов в парламенте, полученных данной партией.
# Названия необходимо выводить в том же порядке, в котором они шли во входных данных.

import sys

stdintext = sys.stdin
partys = []
allvois = 0
for t in stdintext:
    t = t.split()
    party = ' '.join(t[:-1])
    voices = int(t[-1])
    allvois += voices
    partys.append([party, voices, 0, 0])
isb = allvois / 450
free = 450
for party in partys:
    vos = party[1] / isb
    party[2], party[3] = int(vos), vos - int(vos)
    free -= int(vos)

party_dict = {k[0]: k[2] for k in partys}
partys.sort(key=lambda x: (-x[3], x[1]))

for i in range(free):
    party = partys[i][0]
    party_dict[party] += 1

for k, v in party_dict.items():
    print(k, v)