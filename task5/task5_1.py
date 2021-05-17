# Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError


print("start of program execution!!")

try:
    print("IN TRY BLOCK")
    a=input("enter expression:")
    #eval() takes expression as a string, evaluates the expression inside it and returns result
    x=eval(a)       #x holds the result of evaluation from eval()

except SyntaxError:
    print("IN EXCEPT BLOCK")
    print("there is a syntax error")

else:
    print("IN ELSE BLOCK")
    print(type(a))
    print(a) #prints the value stored in 'a' not the result of evaluation from eval()
    print(type(x))
    print(x)

finally:
    print("IN FINALLY BLOCK")
    print("end of program")

#output
#case1: with syntax error
# start of program execution!!
# IN TRY BLOCK
# IN EXCEPT BLOCK
# there is a syntax error
# IN FINALLY BLOCK
# end of program
#
# Process finished with exit code 0
#

#case2: without syntax error
# start of program execution!!
# IN TRY BLOCK
# IN ELSE BLOCK
# <class 'str'>
# 10/2
# <class 'float'>
# 5.0
# IN FINALLY BLOCK
# end of program
#
# Process finished with exit code 0
#case3: accepting input from user
# start of program execution!!
# IN TRY BLOCK
# enter expression:10*
# IN EXCEPT BLOCK
# there is a syntax error
# IN FINALLY BLOCK
# end of program
#
# Process finished with exit code 0
