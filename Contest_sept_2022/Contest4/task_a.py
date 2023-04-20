# В университете есть n аудиторий и m учебных групп. Для каждой аудитории задана её вместимость, а для каждой
# группы — численность. Группа может заниматься в аудитории только если её численность не превосходит
# размера аудитории. Определите максимальное количество групп, которые можно рассадить по аудиториям.

n = int(input())
groups = [int(i) for i in input().split()]
m = int(input())
auditoriums = [int(i) for i in input().split()]
groups.sort()
auditoriums.sort()
res = 0
number = 0
for group in groups:
    while number < m and auditoriums[number] < group:
        number += 1
    if number == m:
        break
    else:
        res += 1
        number += 1
print(res)
