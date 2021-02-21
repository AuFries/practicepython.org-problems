'''
Exercise 5
Randomly generates 2 list (integers 1-50) of random length (1-50) and returns a sorted final list that only contains elements common between them
'''

import random

length1 = random.randint(1,50)
length2 = random.randint(1,50)
list1 = []
list2 = []
common_list = []

for i in range(length1): #generate list 1
    list1.append(random.randint(1,50))

for i in range(length2): #generate list 2
    list2.append(random.randint(1,50))

print("List 1:", list1)
print("List 2:", list2)

for i in range(length1):
    for j in range(length2): #find values that are the same in both lists
        if list1[i] == list2[j]:
            common_list.append(list1[i])

common_list = list(set(common_list)) #removes duplicate values in the list
common_list.sort() #sorts list lowest to highest

print("Common values list:", common_list)
