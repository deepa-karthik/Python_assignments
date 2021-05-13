#10) Generate and print another tuple whose values are even numbers in the given tuple
#(1,2,3,4,5,6,7,8,9,10).

my_tuple=(1,2,3,4,5,6,7,8,9,10)
print(my_tuple)
even_list=[]

for item in my_tuple:
    if item%2==0:
        even_list.append(item)
print(f"even number list:{even_list}")
#use tuple() to return a tuple
even_tuple=tuple(even_list)
print(f"the tuple of even numbers is {even_tuple}")