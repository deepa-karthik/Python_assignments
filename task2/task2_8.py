#8) Write a program that accepts a string as an input from the user and calculate the number of digits
#and letters.
user_input=input("enter a string:")
num_list=["0","1","2","3","4","5","6","7","8","9"]
letter_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter_count=0
digit_count=0

for ch in user_input:
    if ch in num_list:
        digit_count+=1

    if ch in letter_list:
        letter_count+=1

print("the number of alphabets in input string is", letter_count)
print("the number of digits in input string is", digit_count)
