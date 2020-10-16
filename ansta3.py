def half_nums_generator(first, second):
	"""
	Takes two floats and return and array of halfs in between
	"""
	result = []
	x = int(((second-first)*2))
	for i in range(1, x + 2):
		result.append((second-first)*2-second+(i/2))

	return result
print(half_nums_generator(2, 5.5))