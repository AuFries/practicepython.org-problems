'''
Exercise 3
Takes a list of elements and makes new list with all the elements less than 10
'''

start = [1, 1, 2, 3, 5, 8, 13, 21, 34, 4, 89]
less_than_ten = []

for num in start:
    if num < 10:
        less_than_ten.append(num)

print("Starting list:", start)
print("Final list:", less_than_ten)

smaller_than = int(input("Input a number that all numbers must be smaller than in the starting list: "))
smaller_than_list = []

for num in start:
    if num < smaller_than:
        smaller_than_list.append(num)

print("The list with numbers smaller than", smaller_than, "is", smaller_than_list)
