# 7)Write a program that prints all the numbers from 0 to 6 except 3 and 6.

num=0
while num<6:
    if num==3:
         num+=1
         continue
    else:
        print(num,end=" ")
        num+=1

#output:
# 0 1 2 4 5
# Process finished with exit code 0


