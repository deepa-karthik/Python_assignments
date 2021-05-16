# Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

my_str=input("enter a string:").split("-")
print("list after the split at '-' is:",my_str)     #after split

output_str=""           #declare empty string(no whit space) which act as separator for join()
my_str.sort()           #sorts string in alphabetically
print("the sorted list is:",my_str)       #after sort

output_list=[]
for i in range(0,len(my_str)):
    output_list.append(my_str[i])
#if block used to eliminate a'-' at the end of the list during last iteration
    if i!=len(my_str)-1:
        output_list.append("-")
    else:
        break
print("the hyphenated list is :",output_list)      #hyphenated list


output_str=output_str.join(output_list)

print("the sorted string is: ",output_str)

#output
# enter a string:zebra-yak-horse-tiger-apple-banana-cat
# list after the split at '-' is: ['zebra', 'yak', 'horse', 'tiger', 'apple', 'banana', 'cat']
# the sorted list is: ['apple', 'banana', 'cat', 'horse', 'tiger', 'yak', 'zebra']
# the hyphenated list is : ['apple', '-', 'banana', '-', 'cat', '-', 'horse', '-', 'tiger', '-', 'yak', '-', 'zebra']
# the sorted string is:  apple-banana-cat-horse-tiger-yak-zebra
#
# Process finished with exit code 0


