n, k = map(int, input().split())
nums = list(map(int, input().split()))
pref = [0] * n
pref[0] = nums[0]
for i in range(1, n):
    pref[i] = pref[i - 1] + nums[i]

pref_dict = {}
res = 0
for pref_sum in pref:
    if pref_sum == k:
        res += 1
    if pref_sum - k in pref_dict:
        res += pref_dict[pref_sum - k]
    if pref_sum not in pref_dict:
        pref_dict[pref_sum] = 0
    pref_dict[pref_sum] += 1
print(res)
