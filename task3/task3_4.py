#4) Find the largest and smallest number from a given list.

my_list=[10,300,20,400,558,7]

#case 1 :using built-in function
print(max(my_list))
print(min(my_list))

#case2: using logic

max_num=0
min_num=my_list[0]

for item in my_list:
    if item>max_num:
        max_num=item
for item in my_list:
    if item <min_num:
        min_num=item


print("largest number is {}".format(max_num))
print("smallest number is {}".format(min_num))


#output

# 558
# 7
# largest number is 558
# smallest number is 7
#
# Process finished with exit code 0


