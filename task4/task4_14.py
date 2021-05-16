# Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

count=int(input("enter a count:"))
num_list=[]
for item in range(1,count+1):
    num_list.append(item)
print(f"the original list is: {num_list}")

filter_values=filter(lambda x:x%3!=0 and x%7==0,num_list)

print(f"the filtered list is : {list(filter_values)}")

#output:
# enter a count:30
# the original list is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# the filtered list is : [7, 14, 28]
#
# Process finished with exit code 0