# Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).

num_list=[]
new_list=[]         #list to hold 1st 5 and last 5 elements between 1 nd 30 including both numbers
squares_list=[]

#to generate a list of numbers from 1 to 30
for item in range(1,31):
    num_list.append(item)

print(num_list)

#slice the first 5 elements from the list and add to new_list
first5_list=num_list[:5]
print(first5_list)

new_list.extend(first5_list)
print(new_list)

#slice last 5 elements from the list and add to new_list
last5_list=num_list[-5:]
print(last5_list)

new_list.extend(last5_list)
print("the new list of numbers is {}".format(new_list))

#to generate list of squares

for item in new_list:
    squares_list.append(item*item)

print("the list of squares is {}".format(squares_list))

