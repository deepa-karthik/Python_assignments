#Write a program in Python which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200.

for num in range(2000,3000):
    if num%7==0 and num%5!=0:
        print(num)

