from collections import deque


def sum_time_in_pvz(minutes: int, cnt_by_minute: int, arr: list[int]) -> int:
    res = 0
    que = deque()
    for minute in range(minutes):
        cnt = cnt_by_minute
        while que and cnt > 0:
            if que[0][0] <= cnt:
                from_que = que.popleft()
                cnt -= from_que[0]
                res += from_que[0] * (minute - from_que[1] + 1)
            else:
                que[0][0] -= cnt
                res += cnt * (minute - que[0][1] + 1)
                cnt = 0
        current = arr[minute]
        if current > cnt:
            current -= cnt
            res += cnt
            que.append([current, minute])
        else:
            res += current
    for ost in que:
        res += ost[0] * (minutes - ost[1] + 1)

    return res


n, b = map(int, input().split())
a = list(map(int, input().split()))
answer = sum_time_in_pvz(n, b, a)
print(answer)
