# Children inherit the attributes and functions of parent class All animals are a form of mammal and all mammals can
# walk, so instead of repeating a code in each class we can write in the parent class and all children can inherit
# parent properties


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass  # python doesnt like empty class. If you have Dog specific functions you can add that or pass this class


dog1 = Dog()
dog1.bark()
dog1.walk() # dog can inherit parent methods

cat1 =  Cat()
cat1.walk() # cat can inherit parent methods

