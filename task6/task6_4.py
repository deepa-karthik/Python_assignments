# Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”

in_str="Consultadd Training"
print(f"input string is: {in_str}")

#generator function
def rev_str(str):
    x=0
    while x<len(str):
        out_str=""
        out_str=out_str.join(reversed(str))     #returns a reversed iterator
        yield out_str
        x+=1

iter_str=rev_str(in_str)
print(f"the output string is: {next(iter_str)}")


#output
# input string is: Consultadd Training
# the output string is: gniniarT ddatlusnoC
#
# Process finished with exit code 0

# a=[1,2,3,4]
# itr=reversed(a)
# for i in itr:
#     print(i)