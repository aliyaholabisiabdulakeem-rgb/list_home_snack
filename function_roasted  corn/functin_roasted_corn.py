# length_of_string

def length_of_string(string):
    length_of_string = len(string)
    return length_of_string


#first two and last two
def first_two_last_two(string):
    if len(string) < 2:
        return ""
    return string[:2] + string[-2:]

# Adding 'ing' and 'ly'
def add_ing_or_ly(string):
    if len(string) <= 3:
        return string
    if string[-3:] == 'ing':
        return string + 'ly'
    else:
        return(string + 'ing')

# Longest and lenght of a string
#def longest_and_lenght(strings):
 #   longest_string = strings[0]
  #  for count in strings:
   #     if len(string) > len(longest_string):
    #        return longest_string, len(string)


# Odd index of string
def odd_index_of_string(string)
    if string[] % 2 == 1:
        return string
print(length_of_string("semicolon"))
print(first_two_last_two("As"))
print(first_two_last_two("semicolon"))
print(add_ing_or_ly("abc"))
print(add_ing_or_ly("string"))
#print(longest_and_lenght("apple", "corn", "pineapple", "breakfast"))
print(odd_index_of_string(semicolon))

