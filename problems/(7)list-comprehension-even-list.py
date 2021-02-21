'''
Exercise 7
Takes a list and makes 2 new lists with only the odd and even numbers from the original list (practice writing the list modifications on 1 line)
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_list = [num for num in a if num % 2 == 0]
odd_list = [num for num in a if num % 2 != 0]

print("Original list:", a)
print("Even list:", even_list)
print("Odd list:", odd_list)
