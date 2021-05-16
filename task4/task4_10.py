# Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)

my_list=[]
for i in range(1,21):
    my_list.append(i)
print(my_list)

even_list=filter(lambda list1:list1%2==0 ,my_list)
print(list(even_list))

#output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# Process finished with exit code 0
