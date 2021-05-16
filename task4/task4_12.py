# Write a function to compute 5/0 and use try/except to catch the exceptions

num1=int(input("enter a number:"))
num2=int(input("enter another number:"))

try:
    result=num1/num2
    print("the division result is:", result)
except ZeroDivisionError:
    print("number cannot be divided by zero.")

else:
    print("success!")

#output: case1: non zero input
# enter a number:3
# enter another number:3
# the division result is: 1.0
# success!
#
# Process finished with exit code 0

#output: case 2: zero input
# enter a number:5
# enter another number:0
# number cannot be divided by zero.
#
# Process finished with exit code 0


