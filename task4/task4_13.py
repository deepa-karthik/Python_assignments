# Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
new_list=[1,2,3,4,5,6,7]
print(new_list)

def join_str(item1,item2):
    return str(item1)+str(item2)        #str() converts each item to a string

#reduce() takes 2 arguments.. a function and an iterable
#the function should be written in a such a way that it should take 2 arguments only
print(f"the flattened output is :{reduce(join_str,new_list)}")

#output:
# [1, 2, 3, 4, 5, 6, 7]
# the flattened output is :1234567




