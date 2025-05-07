def remove_el(lst, ind):
    prev = lst[ind][1]
    next_ = lst[ind][2]
    if prev is not None:
        lst[prev][2] = next_
    if next_ is not None:
        lst[next_][1] = prev
    lst[ind][1] = None
    lst[ind][2] = None


n = int(input())
ratings = list(map(int, input().split()))
ratings_list = [[ratings[i], i - 1, i + 1] for i in range(n - 1)]
ratings_list[0][1] = n - 1
ratings_list.append([ratings[n - 1], n - 2, 0])
removes = []
for j in range(n):
    rating = ratings[j]
    prev = ratings_list[j][1]
    next_ = ratings_list[j][2]
    if rating < ratings[prev] and rating < ratings[next_]:
        removes.append(j)
prev_cnt = n + 1
cur_cnt = n
round_ = 1
answer = [0] * n

while prev_cnt != cur_cnt and cur_cnt > 2:
    prev_cnt = cur_cnt
    new_removes = []
    for index in removes:
        answer[index] = round_
        cur_cnt -= 1
        prev = ratings_list[index][1]
        next_ = ratings_list[index][2]
        remove_el(ratings_list, index)
        left_raiting = ratings[prev]
        left_prev = ratings_list[prev][1]
        left_next = ratings_list[prev][2]
        if left_raiting < ratings[left_prev] and left_raiting < ratings[left_next]:
            new_removes.append(prev)
        right_raiting = ratings[next_]
        right_prev = ratings_list[next_][1]
        right_next = ratings_list[next_][2]
        if right_raiting < ratings[right_prev] and right_raiting < ratings[right_next]:
            new_removes.append(next_)
    round_ += 1
    removes = new_removes.copy()

print(*answer)
