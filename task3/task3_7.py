#7) Write a program to replace the last element in a list with another list.

list1=[1,2,3,4,5,6]
list2=[10,20,30,40]

print("list1 is",list1)
print("list2 is",list2)

list1.pop(5)
print("list1 with last element removed is",list1)

list1.extend(list2)
print("the updated list is" ,list1)

#output
# list1 is [1, 2, 3, 4, 5, 6]
# list2 is [10, 20, 30, 40]
# list1 with last element removed is [1, 2, 3, 4, 5]
# the updated list is [1, 2, 3, 4, 5, 10, 20, 30, 40]
