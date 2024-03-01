statuses = {"M": "RCD", "R": "C", "C": "M", "D": "M"}
for _ in range(int(input())):
    task = input().strip()
    carrent_status = task[0]
    if carrent_status != "M":
        print("NO")
        continue
    for i in range(1, len(task)):
        new_status = task[i]
        if not (new_status in statuses[carrent_status]):
            print("NO")
            break
        carrent_status = new_status
    else:
        if carrent_status == "D":
            print("YES")
        else:
            print("NO")
