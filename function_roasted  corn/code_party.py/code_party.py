def appending_without_modifying(numbers):
    new_numbers = (4, 6, 7)
    result = numbers + new_numbers
    return result
print(appending_without_modifying((1, 2, 3, 5)))


#def change_elements_in_tuple():
#    numbers = (1, 2, [3, 4], 5)
#    numbers[2][1] = 99
#print(change_elements_in_tuple((numbers)))
#

def even_number(numbers):
    return numbers % 2 == 0
print(list(filter(even_number, range(1, 21))))


def longer_elements(words):
    return len(words) > 5
words = ["cat", "elephant", "tiger", "lion"]
print(list(filter(longer_elements, words)))


def first_value_greater_than_two(lists):
    return lists[0] > 2
lists = [(1, 'A'), (4, 'B'), (2, 'C')]
print(list(filter(first_value_greater_than_two, lists)))


def divisible_by_three_and_five(numbers):
    return numbers % 3 == 0 and numbers % 5 == 0
print(list(filter(divisible_by_three_and_five, range(1, 51))))


def is_palindrome(words):
    return words == words[::-1]
words = ["level", "word", "madam", "python"]
print(list(filter(is_palindrome, words)))


def to_uppercase(words):  
    words = ["python", "java", "c++"]
print(list(map(to_uppercase, words)))


def square(numbers):
    return numbers * numbers
print(list(map(square, range(1, 11))))


def capitalize_first_letters(words):
    return words[0].upper() + words[1:]
words = ["john", "mary", "steve"]
print(list(map(capitalize_first_letters, words)))


def add_ten_percent_tax(prices):
    return prices + prices * 0.10
prices = [100, 200, 300]
print(list(map(add_ten_percent_tax, prices)))


from functools import reduce
def sum_of_numbers(a, b):
    return a + b
print(reduce(sum_of_numbers(1, 51)))


