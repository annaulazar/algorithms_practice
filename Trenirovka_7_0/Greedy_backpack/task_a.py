# A. Каждому по компьютеру
# В новом учебном году во Дворец Творчества Юных для занятий в компьютерных классах пришли учащиеся, которые
# были разбиты на N групп. В i-й группе оказалось Xi  человек. Тут же перед директором встала серьезная
# проблема: как распределить группы по аудиториям. Во дворце имеется M ≥ N аудиторий, в j-й аудитории
# имеется Yj  компьютеров. Для занятий необходимо, чтобы у каждого учащегося был компьютер и еще один
# компьютер был у преподавателя. Переносить компьютеры из одной аудитории в другую запрещается. Помогите
# директору!
# Напишите программу для поиска максимального количества групп, которое удастся одновременно распределить
# по аудиториям, чтобы всем учащимся в каждой группе хватило компьютеров, и при этом остался хотя бы один
# для учителя.


n, m = map(int, input().split())
groups = [(x, ind) for (ind, x) in enumerate(list(map(int, input().split())))]
rooms = [(y, ind) for (ind, y) in enumerate(list(map(int, input().split())))]
groups_res = [-1] * n
groups.sort()
rooms.sort()
res = 0
room_ind = 0
for cnt, group_number in groups:
    need = cnt + 1
    while room_ind < m and rooms[room_ind][0] < need:
        room_ind += 1
    if room_ind <= (m - 1) and rooms[room_ind][0] >= need:
        res += 1
        groups_res[group_number] = rooms[room_ind][1]
        room_ind += 1
    else:
        break
print(res)
for group in groups_res:
    print(group + 1)
