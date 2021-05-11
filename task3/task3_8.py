#8)Create a new dictionary by concatenating the following two dictionaries:

dictA={1:10,2:20,3:30}
dictB={4:40,5:50,6:60,7:70}

print("dictionary A is",dictA)
print("dictionary B is",dictB)

#add the elemetns of dictB to dictA using update()
dictA.update(dictB)
print("the updated dictionary is",dictA)

#output
# dictionary A is {1: 10, 2: 20, 3: 30}
# dictionary B is {4: 40, 5: 50, 6: 60, 7: 70}
# the updated dictionary is {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}
#
# Process finished with exit code 0
