# Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.

num_list=[10,12,33,13,14,100,78,54,77,45]

new_list=[]

for item in num_list:
    if item%2!=0:
        new_list.append(item)


print("the original list {}".format(num_list))
print("the new list is {}".format(new_list))

#output
# the original list [10, 12, 33, 13, 14, 100, 78, 54, 77, 45]
# the new list is [33, 13, 77, 45]

