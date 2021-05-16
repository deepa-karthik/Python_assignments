# Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.

# def max_str(str1,str2):
#     len_str1=len(str1)
#     len_str2=len(str2)
#     if len_str1>len_str2:
#         print(f"the longer string is: {str1}")
#     elif len_str2>len_str1:
#         print(f"the longer string is {str2}")
#     else:
#         print(f"{str1} and {str2} are of equal length.")
#
# user_str1=input("enter a string:")
# user_str2=input("enter another string:")
#
# max_str(user_str1,user_str2)

#output: case 1 : equal length strings
# enter a string:hello
# enter another string:world
# hello and world are of equal length.
#
# Process finished with exit code 0

#output: case 2: unequal string
# enter a string:hi
# enter another string:hello
# the longer string is hello
#
# Process finished with exit code 0

# enter a string:welcome
# enter another string:hi
# the longer string is: welcome
#
# Process finished with exit code 0

#attempt using lamda

user_str1=input("enter a string:")
user_str2=input("enter another string:")
if len(user_str1)!=len(user_str2):
    str_len=lambda x_str,y_str:x_str if len(x_str)>len(y_str) else y_str
    print(f"the longer string is: {str_len(user_str2, user_str1)}")
else:
    print("strings have equal length.")

