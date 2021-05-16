# #Create a function that takes a list and returns a new list with unique elements of the first list.

new_list=[]
list_count=int(input("enter the number of elements in the list:"))

for i in range(0,list_count):
    item=input("enter the list element:")
    new_list.append(item)

print(new_list)

def unique_list(my_list):
    unique_set=set(my_list)
    new_list1=list(unique_set)
    print(f"the list with unique elements is {new_list1}")


unique_list(new_list)



#attempt using lambda()

my_list=[1,2,3,1,2,3,5,6,7,2]

#accepts a list and converts to a set
x=lambda list1:set(list1)

#converts the set to a list and prints to console
print(list(x(my_list)))

#above print is equal to the lines of code below
# my_Set=x(my_list)
# print(my_Set)
# new_list=list(my_Set)
# print(new_list)
#output
#[1, 2, 3, 5, 6, 7]

#output
# enter the number of elements in the list:6
# enter the list element:2
# enter the list element:4
# enter the list element:1
# enter the list element:2
# enter the list element:2
# enter the list element:4
# ['2', '4', '1', '2', '2', '4']
# the list with unique elements is ['2', '4', '1']
#
# Process finished with exit code 0


