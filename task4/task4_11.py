# Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.

#list comprehension method to generate a list

new_list=[x for x in range(1,11)]
print(f"the original list is:{new_list}")

#to generate a list of even numbers

even_list=filter(lambda l:l%2==0,new_list)
#print(list(even_list))

#if the filter object is used for any purpose it completely disappears..
#after printing even_list, it is not available for generating squares list

squares_list=map(lambda y:y*y,even_list)
print(f"the list of squares is: {list(squares_list)}")

#print(list(squares_list),list(even_list))   #output:[] [] as both lists are empty after being used

#output
# the original list is:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# the list of squares is: [4, 16, 36, 64, 100]
#
# Process finished with exit code 0
