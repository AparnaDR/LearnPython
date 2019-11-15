class Point: # naming convention camel caps
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

# object1
point2 = Point()
point2.draw()
print(point2.x) # Error will be displayed as Point class doesnt have any attribute as x. To solve this problem we use
# constructor. Constructor is a function that gets called at the time of creating an object
# apart from methods we can also have attributes, these attributes belong to a particular object
point2.x = 10
point2.y = 20
print(point2.x)
point2.move()

# object2
point2.draw()
print(point2.x)
point2.x = 20 # these attributes belong to only point2
point2.y = 30
print(point2.y)
point2.move()