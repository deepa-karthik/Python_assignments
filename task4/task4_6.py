# Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.

def add(x,y):
    print(type(x),type(y))
    sum=int(x)+int(y)
    print(f"the sum of 2 numbers is: {sum}")

num1=input("enter a number:")
num2=input("enter another number:")

add(num1,num2)

#output
# enter a number:10
# enter another number:29
# <class 'str'> <class 'str'>
# the sum of 2 numbers is: 39
#
# Process finished with exit code 0
