def buble_sort(nums):
	data, n = list(nums), len(nums)
	for i in range(n):
		swap = False
		for j in range(n - i - 1):
			if data[j] > data[j + 1]:
				data[j], data[j + 1] = data[j + 1], data[j]
				swap = True
		if not swap:
			return data
	return data

print(buble_sort([3, 4, 2, 5, 1])) # [1, 2, 3, 4, 5]
