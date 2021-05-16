# # Write a program in Python to multiply the elements of a list by itself using a traditional function
# # and pass the function to map() to complete the operation.
#
# #generate list by asking the user for count
count=int(input("enter a count:"))
num_list=[]
for item in range(0,count+1):
    num_list.append(item)
print(f"the original list is: {num_list}")
#
# #traditional function to multiply a number by itself
def self_mult(item):
    result=item*item
    return result
#
# #higher order function implementation using map() and self_mult()
output=map(self_mult,num_list)
print(f"the expected output list is: {list(output)}")

# #output
# # enter a count:5
# # the original list is: [0, 1, 2, 3, 4, 5]
# # the expected output list is: [0, 1, 4, 9, 16, 25]
# #
# # Process finished with exit code 0
#
