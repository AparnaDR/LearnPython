# getter and setter using decelerators


class Rectangle:
    def __init__(self, width, height):  # attributes
        self.width = width # calling the setter method
        self.height = height

    # getter
    @property
    def width(self):
        print('getting width')
        return self._width
    # setter for the width get method
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width should be >=0")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height should be >=0")
        else:
            self._height = height

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


r1 = Rectangle(10, 20)  # creating an object and passing the attribute

# getter
# print(r1.width) # not a usual method call which contains()

# r1.width = -100

r2 = Rectangle(-2, -3)
