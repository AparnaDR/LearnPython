class Point:  # naming convention CapWords convention.
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")

    def move(self):
        print("move")


# we use classes to define new type
# class simply defines blueprint/ template for creating an object, they are new types
# with this new type we can create object
# object is an instance of a class
# for example class is an blue print of a house
# objects are the actual houses built using those blueprint
# Constructor is a function that gets called at the time of creating an object

# object1
#point2 = Point()
#point2.draw()
# print(point2.x) # Error will be displayed if we dont use constructors, as Point class doesnt have any attribute as x.

point = Point(11,22)
print(point.x)
print(point.y)
