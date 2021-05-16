# Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).

def squares():
    num_squares=[]
    for num in range(1,21):
        num_squares.append(num*num)

    tuple_squares=tuple(num_squares)
    print(f"the tuple of squares is : {tuple_squares}")

squares()

#output:
# the tuple of squares is : (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)
#
# Process finished with exit code 0
