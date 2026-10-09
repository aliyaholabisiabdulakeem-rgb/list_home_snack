numbers = [1, 2, 3, 4, 5]
sum = 0
for index in range(len(numbers)):
    if index % 3 == 2:
        sum += numbers[index]
print(sum)
print()
