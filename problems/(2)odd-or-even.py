'''
Exercise 2
Asks the user for 2 numbers and then prints out whether the numbers are odd or even.
Also determines if the numbers are a multiple of 4 and even divide into eachother
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

num_list = [num1,num2]

for num in num_list: #checks if odd or even and multiple of 4
    if num % 2 == 0:
        print("{n}: Even".format(n = num),end='')
    else:
        print("{n}: Odd".format(n = num),end='')
    if num % 4 == 0:
        print(", multiple of 4",end='')
    print()

if num1 % num2 == 0:
    print("{n1} divides perfectly into {n2}".format(n1 = num1, n2 = num2))
else:
    print("{n1} does NOT divide perfectly into {n2}".format(n1 = num1, n2 = num2))

if num2 % num1 == 0:
    print("{n2} divides perfectly into {n1}".format(n1 = num1, n2 = num2))
else:
    print("{n2} does NOT divide perfectly into {n1}".format(n1 = num1, n2 = num2))
