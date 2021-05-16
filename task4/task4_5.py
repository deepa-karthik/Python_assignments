# Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.

#str=input("enter a sentence:")  #to accept only one line of input

# apprach1:to accept input in multiline
print("enter a multiline input:")
input_list=[input() for i in range(2)] # creates a list of input lines
print(f"the input lines are: {input_list}")

str=" "
str=str.join(input_list)


print(f"the original input is {str}")

upper_str=str.upper()

print(f"the capitalised output is {upper_str}")

# #output
# enter a multiline input:
# hello welcom to python progamming!!!!
# my name is deepa karthik!!!
# the input lines are: ['hello welcom to python progamming!!!!', 'my name is deepa karthik!!!']
# the original input is hello welcom to python progamming!!!! my name is deepa karthik!!!
# the capitalised output is HELLO WELCOM TO PYTHON PROGAMMING!!!! MY NAME IS DEEPA KARTHIK!!!
#
# Process finished with exit code 0


#approach2:

line_count=int(input("enter number of lines:"))
input_list=[]
for i in range(0,line_count):
    line=input("enter a line")
    input_list.append(line)
print(input_list)

str=" "  #declare a string with white space..will be separtor for join()
str=str.join(input_list)


print(f"the original input is {str}")

upper_str=str.upper()

print(f"the capitalised output is {upper_str}")

#output
# enter number of lines:2
# enter a linehello welcome.
# enter a linemy name is deepa
# ['hello welcome.', 'my name is deepa']
# the original input is hello welcome. my name is deepa
# the capitalised output is HELLO WELCOME. MY NAME IS DEEPA