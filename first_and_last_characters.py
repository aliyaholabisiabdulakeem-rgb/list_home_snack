def count_number_of_strings(strings):
    count = 0
    for numbers in strings:
        if len(numbers) >= 2 and numbers[0] == numbers[-1]:
            count += 1
    return count
    
print(count_number_of_strings(['as', 'thirst', '1981']))
