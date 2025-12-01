# J. Аскетизм*
# Вася стал аскетом и решил отказаться от всего материального ради духовного. Действительно, перспектива
# переродиться в желтого земляного червяка из-за утреннего капучино может здорово напугать.
# Однако отказываться от материального оказалось не так-то просто. Для каждого события своей ежедневной
# материальной жизни Вася определил его материальность и обозначил её целым положительным числом mi. Свою
# духовную силу Вася определил как число D. Каждый день он может отказываться от одного события материальной
# жизни и возвращать некоторые события материальной жизни, от которых он отказался ранее, чтобы суммарное
# количество материального снизилось не более чем на D. При этом нельзя делать так, чтобы количество
# материальности в какой-либо день выросло — это собьёт Васю с пути аскезы.
# Вася разработал оптимальный план для себя и стал гуру. Теперь его ученики отказывались от материального
# в пользу Васи. Учеников оказалось очень много, Вася успешно определяет их события материального мира и
# духовную силу, но теперь ему нужна программа, которая будет разрабатывать план отказа от материального.
# В оптимальном плане нужно отказаться от максимального количества событий материальной жизни, а в случае,
# если это возможно сделать несколькими способами, нужно сделать это за наименьшее количество дней.


def get_bag(array, max_value):
    bag = [10**7 + 1] * (max_value + 1)
    bag[0] = 0
    last_ind = 0
    for val in array:
        start_ind = min(last_ind, max_value - val)
        last_ind = start_ind + val
        if val <= d:
            own_days = 1
        else:
            add_val = val - d
            own_days = bag[add_val] + 1

        for j in range(start_ind, -1, -1):
            target_ind = j + val
            new_days = bag[j] + own_days
            if bag[target_ind] > new_days:
                bag[target_ind] = new_days

        for x in range(start_ind + val, 0, -1):
            if bag[x] < bag[x - 1]:
                bag[x - 1] = bag[x]

    return bag


n, d = map(int, input().split())
items_id = {}
items = []
for i in range(1, n + 1):
    row = input().split()
    item = row[0].strip()
    m_ = int(row[1])
    items_id[i] = item
    items.append((m_, i))

items.sort()
removes = []
sum_removes = 0

for y in range(n):
    if items[y][0] <= d + sum_removes:
        removes.append(items[y])
        sum_removes += items[y][0]
    else:
        break

k = len(removes)
days = 0

if k > 0:
    removes_values = [v for v, _ in removes]
    items_bag = get_bag(removes_values, removes_values[-1])
    days = sum([items_bag[v] for v in removes_values])

result = [items_id[key] for _, key in removes]
result.sort()
print(k, days)
for res in result:
    print(res)
