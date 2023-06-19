'''Каждые сутки на вокзал прибывает n электричек. По заданному расписанию прибытия электричек определите
минимальное время между прибытием двух разных электричек.'''

n = int(input())
times = input().split()
times_minutes = []
for time in times:
    h, m = map(int, time.split(':'))
    times_minutes.append(h * 60 + m)
times_minutes.sort()
min_dist = 1440 + times_minutes[0] - times_minutes[-1]
for i in range(1, n):
    min_dist = min(min_dist, times_minutes[i] - times_minutes[i - 1])
print(min_dist)
