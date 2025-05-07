n = int(input())
a = list(map(int, input().split()))
pref_left = [0] * n
pref_right = [0] * n
pref_sum_left = [0] * n
pref_sum_right = [0] * n
for i in range(1, n):
    pref_left[i] = pref_left[i - 1] + a[i - 1]
    pref_sum_left[i] = pref_sum_left[i - 1] + pref_left[i]

for j in range(n - 2, -1, -1):
    pref_right[j] = pref_right[j + 1] + a[j + 1]
    pref_sum_right[j] = pref_sum_right[j + 1] + pref_right[j]

min_transitions = pref_sum_left[0] + pref_sum_right[0]
for k in range(n):
    transitions = pref_sum_left[k] + pref_sum_right[k]
    min_transitions = min(min_transitions, transitions)

print(min_transitions)
