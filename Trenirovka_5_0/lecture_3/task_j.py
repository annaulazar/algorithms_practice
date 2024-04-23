def set_needs() -> list[int]:
    """
    Устанавливает номера части, которую нужно скачать каждому устройству
    """
    # Количество девайсов и номер части для каждой из частей
    parts = [(cnt, index) for index, cnt in enumerate(cnt_devices_by_parts)]
    parts.sort()
    needs = [-1] * n
    for i in range(1, n):
        for _, part in parts:
            if part not in parts_on_devices[i]:
                needs[i] = part
                break
    return needs


def get_reqwests(needs: list[int]) -> list[list[tuple]]:
    """
    Формирует запрос для каждого устройства - [(номер части, с какого устройства запрос), ...] - по индексу устройства к которому запрос
    """
    # Количество частей и номер девайса
    devices = [(cnt, index) for index, cnt in enumerate(cnt_parts_on_devices)]
    devices.sort()
    reqwests = [[] for _ in range(n)]
    for j in range(1, n):
        part = needs[j]
        if part != -1:
            for _, device in devices:
                if device in devices_by_parts[part]:
                    reqwests[device].append((part, j))
                    break
    return reqwests


def allow_reqwests(reqwests: list[list[tuple]]) -> list[tuple]:
    """
    Формирует утвержденные запросы - (номер части, с какого устройства скачивается, на какое устройство)
    """
    allowed = []
    for device in range(n):
        if reqwests[device]:
            if len(reqwests[device]) == 1:
                allowed.append((reqwests[device][0][0], device, reqwests[device][0][1]))
            else:
                reqwests_to_device = {from_device: part for (part, from_device) in reqwests[device]}
                values = []
                for index, value in enumerate(value_devices[device]):
                    values.append((value, cnt_parts_on_devices[index], index))
                values.sort(key=lambda x: (-x[0], x[1], x[2]))
                for value, _, from_device in values:
                    if from_device in reqwests_to_device:
                        allowed.append((reqwests_to_device[from_device], device, from_device))
                        break
    return allowed


def make_reqwests(allowed) -> None:
    """
    Удовлетворяет одобренные запросы, меняя данные в соответствующих структурах
    """
    global complete
    for part, from_device, to_device in allowed:
        value_devices[to_device][from_device] += 1
        parts_on_devices[to_device].add(part)
        cnt_parts_on_devices[to_device] += 1
        if cnt_parts_on_devices[to_device] == k:
            complete += 1
            compleet_devices[to_device] = 1
        devices_by_parts[part].add(to_device)
        cnt_devices_by_parts[part] += 1


n, k = map(int, input().split())

# Ценность каждого из устройств (внутренний массив) для устройства по индексу внешнего массива
value_devices = [[0] * n for _ in range(n)]
# Массив скачанных частей на каждом из устройств
parts_on_devices = [set() for _ in range(n)]
parts_on_devices[0] = set(range(k))
# Количество скачанных частей на каждом из устройств
cnt_parts_on_devices = [0] * n
cnt_parts_on_devices[0] = k
# Массив устройств на которых есть данная часть
devices_by_parts = [{0} for _ in range(k)]
# Количество устройств, на которых есть данная часть
cnt_devices_by_parts = [1 for _ in range(k)]

time_slots = [0] * n # Количество тайм-слотов, для каждого девайса
compleet_devices = [0] * n
compleet_devices[0] = 1
complete = 1
while complete < n:
    for y in range(n):
        if compleet_devices[y] == 0:
            time_slots[y] += 1
    devices_needs = set_needs()
    reqwest_parts = get_reqwests(devices_needs)
    allowed_reqwests = allow_reqwests(reqwest_parts)
    make_reqwests(allowed_reqwests)

print(*time_slots[1:])
