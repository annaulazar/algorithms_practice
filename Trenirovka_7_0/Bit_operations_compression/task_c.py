def reordering_xor(arr, n_):
    z = len(bin(max(a))) - 2
    cnt_ones_for_numbers = [[bin(x).count('1'), ind] for ind, x in enumerate(arr)]
    cnt_ones_all = sum([el[0] for el in cnt_ones_for_numbers])
    if cnt_ones_all % 2:
        return None
    res = [[0] * z for _ in range(n_)]
    for bit in range(z):
        taken_numbers = [num for num in cnt_ones_for_numbers if num[0] > 0]
        taken_numbers.sort()
        left = 0
        right = len(taken_numbers) - 1
        while left < right:
            _, number_ind = taken_numbers[left]
            res[number_ind][bit] = 1
            cnt_ones_for_numbers[number_ind][0] -= 1
            _, number_ind = taken_numbers[right]
            res[number_ind][bit] = 1
            cnt_ones_for_numbers[number_ind][0] -= 1
            left += 1
            right -= 1

    if any(y[0] != 0 for y in cnt_ones_for_numbers):
        return None

    return [int(''.join(map(str, row)), 2) for row in res]


n = int(input())
a = list(map(int, input().split()))
answer = reordering_xor(a, n)
if not answer:
    print('impossible')
else:
    print(*answer)
