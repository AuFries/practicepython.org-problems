'''
Exercise 6
Asks the user for a string and prints whether or not the string is a palindrome (same word backwards and forwards)
'''

word = input("Enter a word to check whether or not it's a palindrome: ")

reverse_word = ""

for i in range(len(word)-1,-1,-1):
    reverse_word += word[i]

if word == reverse_word:
    print(word,"is a palindrome!")
else:
    print(word,"is not a palindrome.")
