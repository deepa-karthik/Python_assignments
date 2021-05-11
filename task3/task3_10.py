# Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.

#to generate a list from comma separated inputs from console
new_list=input("enter numbers:").split(",")

#creates a list by default
print(new_list)
print(type(new_list))

#tuple() will return a tuple of elements specified in ()
new_tuple=tuple(new_list)
print(new_tuple)
print(type(new_tuple))

#output
# enter numbers:1,2,2,3,4,5
# ['1', '2', '2', '3', '4', '5']
# <class 'list'>
# ('1', '2', '2', '3', '4', '5')
# <class 'tuple'>






