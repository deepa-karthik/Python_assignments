#2)Create a list of thousand numbers using range and xrange and see the difference between each
#other.

# use of range()..generate the desired seqquence of numbers.. it is an obj of range class not list class

# for number in range(1,1001):
#     print(number,end=" ")

num=range(5)
print(num,type(num))
it=iter(num)            #make num as an iterable objet
print(next(it))         #use next() to print the elements
print(next(it))
print(next(it))
print(next(it))
print(next(it))


