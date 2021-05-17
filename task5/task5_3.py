# Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”


try:
    num = input("enter a 4 digit number:")
    if len(num) < 4 or len(num) > 4:
        raise ValueError


except ValueError:
    print("the length id too long/short. pls provide only 4 digits!!")

else:
    print("else block entered")
    print(num)


#output
#case 1:invalid input
# enter a 4 digit number:12345
# the length id too long/short. pls provide only 4 digits!!
#
# Process finished with exit code 0

#case 2:invalid input
# enter a 4 digit number:12
# the length id too long/short. pls provide only 4 digits!!
#
# Process finished with exit code 0

#case 3: valid input
# enter a 4 digit number:1223
# else block entered
# 1223
#
# Process finished with exit code 0



