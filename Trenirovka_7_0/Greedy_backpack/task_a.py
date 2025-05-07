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
