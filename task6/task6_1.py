# Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.

my_string=list(input("enter a string:"))
print(f"the original list is :{my_string}")

output_list=[ch for ch in my_string if ch.isupper()]
print(f"the list of upper case character is:{output_list}")

#output
# enter a string:aBcDeFgHiJkLmNoPqRsTuVwXyZ
# the original list is :['a', 'B', 'c', 'D', 'e', 'F', 'g', 'H', 'i', 'J', 'k', 'L', 'm', 'N', 'o', 'P', 'q', 'R', 's', 'T', 'u', 'V', 'w', 'X', 'y', 'Z']
# the list of upper case character is:['B', 'D', 'F', 'H', 'J', 'L', 'N', 'P', 'R', 'T', 'V', 'X', 'Z']
#
# Process finished with exit code 0
