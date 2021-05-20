# Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]
import itertools

class SumZero:
    def __init__(self,input_list):
        self.input_list=input_list


    def calc_sum(self):
        #returns a tuple which contains 3 elements in different combinations without repetitions
        combo_list = itertools.combinations(self.input_list, 3)
        sum_list=0
        output_list=[]
        #loop to use each tuple of 3 elements and find if its sum is 0
        for item in combo_list:
            #print(item,type(item))
            sum_list=sum(item)
            #print(sum_list)
            if sum_list==0:
               # print(item)
                 output_list.append(item)

        print(f"the expected output is : {output_list}")


input_list=[-25,-10,-7,-3,2,4,8,10]
print(f"the input list is: {input_list}")
#creating object of the class
sum_zero_obj1=SumZero(input_list)
#calling the method to get the expected output
sum_zero_obj1.calc_sum()

#output
# the input list is: [-25, -10, -7, -3, 2, 4, 8, 10]
# the expected output is : [(-10, 2, 8), (-7, -3, 10)]
#
# Process finished with exit code 0
