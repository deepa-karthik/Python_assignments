# Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.

my_str=input("enter a string:")

def lettercase_Count(string):
    upper_count=0
    lower_count=0
    for ch in string:
        if ch.isupper():
            upper_count+=1
        else:
            lower_count+=1
    print(f"No.of uppercase letters is {upper_count}, no.of lowercase letters is{lower_count}")


lettercase_Count(my_str)

#output
# enter a string:abcSdefPghijQkl
# No.of uppercase letters is 3, no.of lowercase letters is12



