def insertion_sort(nums):
	data, n = list(nums), len(nums)
	for i in range(1, n):
		key = data[i]
		j = i - 1
		while j >= 0 and key < data[j]:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key
	return data

print(insertion_sort([3, 4, 2, 5, 1])) # [1, 2, 3, 4, 5]
