# Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
#counter=1
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.


import random

guess_chance=5
guess_count=1

while guess_count<=guess_chance:
    secret_num = random.randint(0, 9)
    print(secret_num)
    user_choice=int(input("guess a number between 0 and 9:"))
    if user_choice==secret_num:
        print("good guess")
        guess_count+=1
        continue

    else:
        print("try again")
        guess_count+=1
        continue

print("game over")

#output
#case1: incorrect guesses
# 1
# guess a number between 0 and 9:2
# try again
# 5
# guess a number between 0 and 9:1
# try again
# 0
# guess a number between 0 and 9:3
# try again
# 3
# guess a number between 0 and 9:5
# try again
# 7
# guess a number between 0 and 9:6
# try again
# game over

#Process finished with exit code 0

# Process finished with exit code 0

#case2: with correct guess

# 7
# guess a number between 0 and 9:7
# good guess
# 5
# guess a number between 0 and 9:6
# try again
# 8
# guess a number between 0 and 9:8
# good guess
# 2
# guess a number between 0 and 9:2
# good guess
# 3
# guess a number between 0 and 9:3
# good guess
# game over
# Process finished with exit code 0