# 7)Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]

num_list=[1,2,3,4,5,6,7,8,9,-1,-2]
sum_number=int(input("enter a number for the sum:"))

list_len=len(num_list)
i=0

while i<list_len:
    for j in range(0,list_len):
        if num_list[i]+num_list[j]==sum_number:
            print(f"the pair of numbers which add to {sum_number} are {num_list[i]},{num_list[j]}")
    i+=1

#output
# enter a number for the sum:8
# the pair of numbers which add to 8 are 1,7
# the pair of numbers which add to 8 are 2,6
# the pair of numbers which add to 8 are 3,5
# the pair of numbers which add to 8 are 4,4
# the pair of numbers which add to 8 are 5,3
# the pair of numbers which add to 8 are 6,2
# the pair of numbers which add to 8 are 7,1
# the pair of numbers which add to 8 are 9,-1
# the pair of numbers which add to 8 are -1,9
#
# Process finished with exit code 0
