#1) Create three variables in a single line and assign values to them in such a manner that each one of
#them belongs to a different data type.

name,age,salary="deepa",60,200.00

print(type(name))
print(type(age))
print(type(salary))


# output
# <class 'str'>
# <class 'int'>
# <class 'float'>

#2)Create a variable of type complex and swap it with another variable of type integer.

num1= 4+5j
print(type(num1))

num2=100
print(type(num2))

print(f"the original numbers are:{num1}, {num2}")

num1,num2=num2,num1

print(f"the original numbers are:{num1}, {num2}")

# output
# <class 'complex'>
# <class 'int'>
# the original numbers are:(4+5j), 100
# the original numbers are:100, (4+5j)

#3)Swap two numbers using a third variable and do the same task without using any third variable.

number1=100
number2=200

print("the numbers before swapping are:", number1,number2)

temp=number2
number2=number1
number1=temp

print("the numbers after swapping are:",number1,number2)

# output
# the numbers before swapping are: 100 200
# the numbers after swapping are: 200 100


#4)Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
#Version.

message=input("enter a message:")
print(message)

#output
# enter a message:hello
# hello

#5)Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

n1=int(input("enter a number between 1 -10: "))
n2=int(input("enter another number between 1 -10: "))
z=n1+n2
result=z+30
print("final output=",result)

#output
# enter a number between 1 -10: 3
# enter another number between 1 -10: 3
# final output= 36

#6)Write a program to check the data type of the entered values.

x=100
y= 45.38
z= "python training"
a = True

print(f"the data type of entered values are {type(x)},{type(y)},{type(z)},{type(a)}")

#output

#the data type of entered values are <class 'int'>,<class 'float'>,<class 'str'>,<class 'bool'>

#7)Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.

# MyName="deepa" #upper camelcase
# myName="karthik" #lower camelcase
# MYNAME="lakshmi"    #upper case
# myname="DEEPA"      #lower case
# my_name="KARTHIK"   #snake case

#8)If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?

#the variable 'a' is pointer to the value assigned to it. when a value is assigned to 'a',an object is created and when
#the variable is 'a' is reassigned,'a' points to the new value. the old value is not deleted from memory.