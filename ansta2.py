def find_missing_elements(array, n):
	"""
	Takes an array of ints and returns an array of missing
	numbers from 1 to n
	"""

	missing_numbers = []
	for i in range(1, n+1):
		if i not in array:
			missing_numbers.append(i)

	return missing_numbers

print(find_missing_elements([2,3,7,4,9], 10))
