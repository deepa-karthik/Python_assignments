# Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).

n=int(input("enter a number to generate a dictionary:"))

dict_result={}
for num in range(1,n+1):
    #print(num)    #checking for range functionality
    dict_result.update({num:num*num})

print("the required dictionary is:",dict_result)


#output
# enter a number to generate a dictionary:5
# the required dictionary is: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

