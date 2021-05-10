# In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.

import random

guess_chance=5
guess_count=1

while guess_count<=guess_chance:
    secret_num = random.randint(0, 9)
    print(secret_num)
    user_choice=int(input("guess a number between 0 and 9:"))
    if user_choice==secret_num:
        print("good guess")
        break

    else:
        print("try again")
        guess_count+=1
        continue
if guess_count==6:
    print("sorry but that was not very sucessful")

#output
#case 1: with correct guess in first chance
# 2
# guess a number between 0 and 9:2
# good guess
#
# Process finished with exit code 0

#case 2: with a correct guess in other chances
# 7
# guess a number between 0 and 9:2
# try again
# 1
# guess a number between 0 and 9:3
# try again
# 4
# guess a number between 0 and 9:4
# good guess

#case 3: with incorrect guess and all chance taken
# 8
# guess a number between 0 and 9:1
# try again
# 9
# guess a number between 0 and 9:1
# try again
# 9
# guess a number between 0 and 9:1
# try again
# 5
# guess a number between 0 and 9:2
# try again
# 1
# guess a number between 0 and 9:2
# try again
# sorry but that was not very sucessful
#
# Process finished with exit code 0