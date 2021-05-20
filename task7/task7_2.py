# Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.

class Shape:
    def area(self):
        shape_area=0
        print(f"the area of the shape is {shape_area}")

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        square_area=self.length*self.length
        print(f"the area of a square is {square_area} square units")

#creating shape object
shape_obj=Shape()
shape_obj.area()
print("")

#creating square object
square_obj=Square(5)
square_obj.area()

#output
# the area of the shape is 0
#
# the area of a square is 25 square units
#
# Process finished with exit code 0

