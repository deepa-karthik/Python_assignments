# Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

import math

def calculate(d):
    H=30
    C=50
    D=int(d)
    result=(2*C*D)/H
    Q=math.sqrt(result)
    return Q
#splits the input string at' ,' and creates a list
value_list=input("enter numbers:").split(",")
print(f"the input numbers are {value_list}")

output=map(calculate,value_list)
print(f"the expected output is {list(output)}")

#output
# enter numbers:1,2,3,4,5
# the input numbers are ['1', '2', '3', '4', '5']
# the expected output is [1.8257418583505538, 2.581988897471611, 3.1622776601683795, 3.6514837167011076, 4.08248290463863]
#
# Process finished with exit code 0
