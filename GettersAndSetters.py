# ## Getters and Setters in Python the Java type
# Getters and setters are used so that you dont give any user access to the attributes directly
# in Java usually they are private variables in class, so you use getters and setters to assign a value to your object
# in Python there is not private variable concept, instead its only convention, whenever you put _ before your variable
# its understood that its a private, but still user can access those variables

class Rectangle:
    def __init__(self, width, height):  # attributes
        self._width = width
        self._height = height

    # getters and setters for width attribute
    def get_width(self):
        return self._width # get has to return the updated width

    def set_width(self,width): # used to set a width, update the width attribute
        if width <= 0:
            raise ValueError('width must be more than 0')
        else:
            self._width = width

    # getters and setters for height attribute
    def get_height(self):
        return self._height  # get has to return the updated height

    def set_height(self, height):  # used to set a height, update the width attribute
        if height <= 0:
            raise ValueError('height must be more than 0')
        else:
            self._height = height

    def __str__(self):
        return 'Rectangle: width = {0} , height = {1}'.format(self._width, self._height)

    def __eq__(self, other):  # comparing 2 objects for equals r1 = self , r2 = other
        # here we need to check if other if the other object is of type rectangle , only then equals should be checked
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False

    def __lt__(self, other):  # comparing 2 objects  for less than r1 = self , r2 = other
        # here we need to check if other if the other object is of type rectangle , only then equals should be checked
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)  # creating an object and passing the attributes

r1._width = 101
print(r1._width) # even though we have used _ we still can modify as its only a convention

# usually we need to provide setters method to modify a class attribute

r1.get_height()
r1.set_height(105)