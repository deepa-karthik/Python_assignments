#8)Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.

even_list=[]
odd_list=[]
lists_count=10
even_sum=0
odd_sum=0

i=0

while i <lists_count:
    number = int(input("enter a number between 1-50"))
    i += 1
    if number%2==0:
        even_list.append(number)
        if len(even_list)==5:
            print("even list reached limit")
        else:
            continue

    else:
        odd_list.append(number)
        if len(odd_list) == 5:
            print("odd list reached limit")
        else:
            continue


max_num_even=max(even_list)
max_num_odd = max(odd_list)
print(f"the max num in even list {even_list} is {max_num_even}")
print(f"the max num in odd list {odd_list} is {max_num_odd}")

for item in even_list:
    even_sum+=item

for item in odd_list:
    odd_sum+=item

print(f"the sum of even_list is {even_sum}")
print(f"the sum of odd list is {odd_sum}")




