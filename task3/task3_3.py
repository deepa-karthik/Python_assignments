#3)Write a program to get the sum and multiply of all the items in a given list.

num_list=[100,25,47,3,93]

sum=0
product=1

for item in num_list:
    sum+=item
    product*=item

print("sum=", sum)
print("product=",product)

#output
# sum= 268
# product= 32782500
#
# Process finished with exit code 0