# Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def show_numbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(f"{i}:EVEN")
        else:
            print(f"{i}:ODD")

num_limit=int(input("enter the limit:"))
show_numbers(num_limit)

#output
# enter the limit:5
# 0:EVEN
# 1:ODD
# 2:EVEN
# 3:ODD
# 4:EVEN
# 5:ODD
#
# Process finished with exit code 0
