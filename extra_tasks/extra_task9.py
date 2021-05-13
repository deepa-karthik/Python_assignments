# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.


#counting occurance of 1 character at a time only
# str="12abcbacbaba344ab"
# count=0
# char=input("enter a character:")
#
# for item in str:
#     if item==char:
#         count+=1
#
# print(f"{char}={count}")

#output
# enter a character:a
# a=5


#counting all occurences of all characters except numbers

str1="12abcbacbaba344ab"
print(f"the original string is {str1}")
num_list=['0','1','2','3','4','5','6','7','8','9']
str_list=[]

#to convert string to a list
for ch in str1:
    if ch not in num_list:
         str_list.append(ch)
print(f"the list without numbers is {str_list}")

#identifies unique characters from list by using set(iterable)

unique_set=set(str_list)
print(f"the set of unique characters is {unique_set}")
print(type(unique_set))

#converts the set to a list so that it can be indexed
unique_list=list(unique_set)
print(f"the unique list of characters is {unique_list}")
print(type(unique_list))

for i in range(0,len(unique_list)):     #loop through the unique list
    count = 0
    for j in range(0,len(str_list)):            #loop through the list with only letters
        if str_list[j]==unique_list[i]:
            count+=1
    print(f"the count of {unique_list[i]} is {count} ")

#output
# the original string is 12abcbacbaba344ab
# the list without numbers is ['a', 'b', 'c', 'b', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'b']
# the set of unique characters is {'b', 'a', 'c'}
# <class 'set'>
# the unique list of characters is ['b', 'a', 'c']
# <class 'list'>
# the count of b is 5
# the count of a is 5
# the count of c is 2
#
# Process finished with exit code 0

