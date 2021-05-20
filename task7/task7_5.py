# Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.

class Person:
    def __init__(self,age):
        if age>0:
            self.age=age
        else:
            print("age is not valid!! setting age to 0")
            self.age=0

    def year_passes(self,age_count):
        print(f"the expected age is: {self.age+age_count}")

    def am_I_old(self):
        if self.age<13:
            print("You are too young!")

        elif self.age>=13 and self.age<19:
            print("You are a teenager!")

        else:
            print("You are old!")

#p1=Person(0)
#output
# age is not valid!! setting age to 0
#
# Process finished with exit code 0

p2=Person(10)
p2.am_I_old()
p2.year_passes(3)

#output
# You are too young!
# the expected age is: 13
#
# Process finished with exit code 0

p3=Person(15)
p3.am_I_old()
p3.year_passes(3)
# #output
# You are a teenager!
# the expected age is: 18
#
# Process finished with exit code 0
p4=Person(20)
p4.am_I_old()
p4.year_passes(3)

#output
# You are old!
# the expected age is: 23
#
# Process finished with exit code 0


