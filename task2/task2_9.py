# 9)Read the two parts of the question below:
# a)Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
# b)Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)

# import random
#
# secret_num= random.randint(0,9)
# print(secret_num)
#
# while True:
#     user_guess = int(input("guess the lucky number:"))
#     if user_guess==secret_num:
#         print("your guess is right")
#         break
#     else:
#         continue
#output:
#case1: number guessed correctly
# 9
# guess the lucky number:9
# your guess is right
#Process finished with exit code 0

#case2: incorrect guess
# 9
# guess the lucky number:3
# guess the lucky number:1
# guess the lucky number:2
# guess the lucky number:4
# guess the lucky number:5
# guess the lucky number:6
# guess the lucky number:7
# guess the lucky number:9
# your guess is right
#
# Process finished with exit code 0

import random

secret_num= random.randint(0,9)
print(secret_num)

while True:
    user_guess = int(input("guess the lucky number:"))
    if user_guess==secret_num:
        print("your guess is right")
        break
    else:
        user_choice= input("do you want to play again? yes/no:")
        if user_choice.lower()=="yes":
            continue
        else:
            print("good game!bye")
            break


#output:
#case1: correct guess
# 5
# guess the lucky number:5
# your guess is right
#
# Process finished with exit code 0

#case2: incorrect guess with user answer
# 9
# guess the lucky number:3
# do you want to play again? yes/no:yes
# guess the lucky number:4
# do you want to play again? yes/no:yes
# guess the lucky number:0
# do you want to play again? yes/no:no
# good game!bye
#
# Process finished with exit code 0
