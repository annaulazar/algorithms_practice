def selection_sort(nums):
	data, n = list(nums), len(nums)
	for i in range(n - 1):
		min_index = i
		for j in range(i + 1, n):
			if data[j] < data[min_index]:
				min_index = j
		data[i], data[min_index] = data[min_index], data[i]
	return data

print(selection_sort([3, 4, 2, 5, 1])) # [1, 2, 3, 4, 5]
