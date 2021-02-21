'''
Exercise 4
Asks the user for a number and prints out a list of all the divisors for that number
'''

x = int(input("Enter a number to calculate the divisors for: "))
divisor_list = []

for num in range(1,x+1):
    if x % num == 0:
        divisor_list.append(num)

print("The list of divisors is:", divisor_list)
