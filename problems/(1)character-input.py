'''
Exercise 1
Asks user's name and age, then prints out the year they will be 100
'''
name = input("What is your name? ")
age = int(input("What is your age? "))
years = 100 - age

years = abs(years)

if age < 100:
    print("{n} will be 100 years old in {y} years.".format(n = name, y = years))
elif age > 100 :
    print("{n} is already over 100 years old!".format(n = name))
else:
    print("{n} is exactly 100 years old.".format(n = name))
