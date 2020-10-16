def postcode_generator(first, second):
	"""
	Takes two postcodes and generates array of postcodes in between
	"""
	postcode_list = []

	first = first.split('-')
	second = second.split('-')
	difference = range(int(first[0]), int(second[0]))

	for i in range(int(first[0]), int(second[0])):
		
			for j in range(int(first[1]), 1000):
				postcode_list.append(f"{first[0]}-{j}")

			for k in range(int(second[1]), 1000):
				postcode_list.append(f"{second[0]}-{j}")
		 

	return postcode_list

print(postcode_generator("79-900", "80-155"))