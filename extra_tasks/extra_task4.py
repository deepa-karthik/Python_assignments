# 4)Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.

for num in range(1,101):
    if num%3==0 and num%2==0:
        print(num, end=" ")

#output
# 6 12 18 24 30 36 42 48 54 60 66 72 78 84 90 96
# Process finished with exit code 0
