# 5)Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
# string with their index.

new_string=input("enter a string:")

rev_string=new_string[::-1]

print(f"the reversed string is {rev_string}")
str_len=len(new_string)

for i in range(str_len):
    #print(new_string[i])
    if new_string[i]=="a"or new_string[i]=="e"or new_string[i]=="i"or new_string[i]=="o"or new_string[i]=="u":
        print(f"the vowel {new_string[i]} is at index {i}")


#output
# enter a string:python training
# the reversed string is gniniart nohtyp
# the vowel o is at index 4
# the vowel a is at index 9
# the vowel i is at index 10
# the vowel i is at index 12
#
# Process finished with exit code 0


