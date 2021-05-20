# Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes

    def add_time(self,object2):         #method will take 2 objects self and object2

        hours_sum = self.hours + object2.hours
        minutes_sum=self.minutes+object2.minutes
        if minutes_sum>=60:             #if min>60 , hour shd be incremented by 1
            hours_sum+=1
            minutes_sum=minutes_sum-60

        print(f"the sum of time is {hours_sum}hr and {minutes_sum}min")

    def display_time(self):
        print(f"the time is {self.hours}:{self.minutes}")

    def display_minute(self):
        total_min=self.hours*60 + self.minutes
        print(f"the total minutes is {total_min} min!!!")

#objects of time class
t1=Time(1,50)
t2=Time(2,20)
t1.add_time(t2)    #calling method with obj1 and passing obj2
#calling metod to display time with each object
t1.display_time()
t2.display_time()

#calling method to calculate total minutes
t1.display_minute()
t2.display_minute()


#output
#case1: minutes adds upto number less than 60
# the sum of time is 3hr and 50min
# the time is 1:30
# the time is 2:20
# the total minutes is 90 min!!!
# the total minutes is 140 min!!!
#
# Process finished with exit code 0

#case2: minute adds upto more than 60
# the sum of time is 4hr and 10min
# the time is 1:50
# the time is 2:20
# the total minutes is 110 min!!!
# the total minutes is 140 min!!!
#
# Process finished with exit code 0
