# Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

print("Welcome to MyLogin Page!!")

user_name=input("USERNAME: ")
password=input("PASSWORD: ")
chance=1
while chance<=3:
    retype_pass = input("RE TYPE PASSWORD: ")
    if retype_pass==password:
        print("LOGIN SUCCESSFUL")
        break
    else:
        print("PASSWORD DOES NOT MATCH")
        chance+=1
        continue

if chance==4:
    print("3 WRONG ATTEMPTS")
    print("LOGIN UNSUCCESSFUL")

#output
#case 1: correct password
# Welcome to MyLogin Page!!
# USERNAME: deepa
# PASSWORD: abcd
# RE TYPE PASSWORD: abcd
# LOGIN SUCCESSFUL
#
# Process finished with exit code 0

#case 2: invcorrect password
# Welcome to MyLogin Page!!
# USERNAME: deepa
# PASSWORD: abcd
# RE TYPE PASSWORD: dskf
# PASSWORD DOES NOT MATCH
# RE TYPE PASSWORD: kdfd
# PASSWORD DOES NOT MATCH
# RE TYPE PASSWORD: ssds
# PASSWORD DOES NOT MATCH
# 3 WRONG ATTEMPTS
# LOGIN UNSUCCESSFUL
#
# Process finished with exit code 0


