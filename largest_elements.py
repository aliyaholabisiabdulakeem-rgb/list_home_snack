def largest_element(string):

	largest = string[0]
	
	for number in string:
		if number > largest:
			largest = number
	return largest
	
print(largest_element([1,2,3,4,5]))
	
