#Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
#
# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.

user_choice=int(input("enter a choice:\n1:Addition\n2:Subtraction\n3:multiplication\n4:Division\n5:Average:\n"))
num1= int(input("enter number 1:"))
num2=int(input("enter number 2:"))

if user_choice==1:
   result= num1+num2
elif user_choice==2:
    result=num1-num2
elif user_choice==3:
    result=num1*num2
elif user_choice==4:
    result=num1/num2
elif user_choice==5:
    x=int(input("enter another number1:"))
    y=int(input("enter another number 2:"))
    total_sum=num1+num2+x+y
    result=(total_sum)/4
else:
    print("invalid input")

if result<0:
    print("NEGATIVE")
else:
    print(result)

#output
# 1:Addition
# 2:Subtraction
# 3:multiplication
# 4:Division
# 5:Average
# 1
# enter number 1:2
# enter number 2:3
# 5

# 2
# enter number 1:2
# enter number 2:1
# 1

# 3
# enter number 1:2
# enter number 2:3
# 6

# 4
# enter number 1:4
# enter number 2:2
# 2.0

# 5
# enter number 1:2
# enter number 2:3
# enter another number1:4
# enter another number 2:5
# 3.5

# 2
# enter number 1:6
# enter number 2:10
# NEGATIVE






