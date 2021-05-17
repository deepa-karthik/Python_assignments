# Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.

import sys

#argv is command to accept input from command line.. argv[1] reads the file name to be opened
file_name=sys.argv[1]

try:
    if  file_name=="task5_2_argv_demo":
        print("file opening success")
        f=open("task5_2_argv_demo.txt","r")
        print(f.readlines())
    else:
        raise NameError

except NameError:
    print("IN EXCEPT BLOCK")
    print("incorrect file name")


