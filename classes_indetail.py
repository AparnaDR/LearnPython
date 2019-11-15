# Classes
# dunder init method is called once the object is created
# self is an instance thats created


class Rectangle:
    def __init__(self, width, height):  # attributes
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def to_string(self):
        return 'Rectangle: width = {0} , height = {1}'.format(self.width, self.height)

    def __str__(self):
        return 'Rectangle: width = {0} , height = {1}'.format(self.width, self.height)

    def __eq__(self, other):  # comparing 2 objects for equals r1 = self , r2 = other
        # here we need to check if other if the other object is of type rectangle , only then equals should be checked
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):  # comparing 2 objects  for less than r1 = self , r2 = other
        # here we need to check if other if the other object is of type rectangle , only then equals should be checked
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)  # creating an object and passing the attributes
print(r1.width)  # printing the attributes
r1.width = 100  # updating the attributes
print(r1.width)  # accessing the methods of a class
print(r1.area())
print(r1.perimeter())

# #### comment the __str__ method in the above class before executing below line
# here we get the memory name of the class, to override and provide our own definition
print(str(r1))
print(hex(id(r1)))
print(r1.to_string())

# to override the above standard str method we can use __str__ method and provide our definition
# #### UN-COMMENT the __str__ method in the above class before executing below line
print(str(r1))
print(r1)

# creating another instance for the same class having same height and width
r2 = Rectangle(100, 20)

# #### comment the __eq__ method in the above class before executing below line
# r1 and r2 are same as its height and width are same, but to the interpreter they both are in different memory location
print(r1 is not r2)  # will return True, which is expected
print('When equal method is not overridden')
print(r1 == r2)  # False, but as a user we expect it to show true, we can override the equals function as well

# #### UN-COMMENT the __eq__ method in the above class before executing below line
print(r1 is not r2)  # will return True, which is expected
print('equals overriding')
print(r1 == r2)

# if equals method in the above class is not checking for the type then we will get error
# remove the if condition in __eq__method and run below code.
# r1 == 100

# Overriding less than method

r3 = Rectangle(10, 20)
r4 = Rectangle(100, 20)
print('Less than overriding')
print(r3 < r4)
print('Greater than is automatically overridden')
print(r3 > r4)  # automatically works as less than is implemented

# we can override <= >= != depending on our project needs
# if we dont implement and we try to compare we will get error
# print(r3 <= r4) # TypeError: '<=' not supported between instances of 'Rectangle' and 'Rectangle'




