#Write a program in Python to break and continue if the following cases occurs:
#If user enters a  negative number just break the loop and print “It’s Over”
#If  user enters a positive number just continue the loop and print “Good going”

i=0
while i<=5:
    number=int(input("enter a number"))
    if number>0:
        print("Good going")
        continue
    else:
        print("It's over")
        break



