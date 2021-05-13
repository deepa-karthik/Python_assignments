# 6)Write a program in Python to iterate through the string “hello my name is abcde” and print the
# string which is having an even length.


str1=input("enter a string:")

word_list=str1.split(" ")
#print(word_list)  #to generate a list with words from the string

for word in word_list:
    if len(word)%2==0:
        print(word)



#output:
# enter a string:hello my name is deepa karthik
# my
# name
# is
