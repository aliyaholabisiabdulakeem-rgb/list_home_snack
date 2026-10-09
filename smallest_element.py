def smallest_element(string):

	smallest = string[0]
	
	for number in string:
		if number < smallest:
			smallest = number
	return smallest
	
print(smallest_element([1,2,3,4,5]))
	
