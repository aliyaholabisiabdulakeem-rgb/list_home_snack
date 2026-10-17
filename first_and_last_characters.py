def count_number_of_strings(strings):
    count = 0
    for letters in strings:
        if len(letters) >= 2 and letters[0] == letters[-1]:
            count += 1
    return count
    
print(count_number_of_strings(['as', 'thirst', '1981']))
