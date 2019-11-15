import decimal

"""
any object that can be called using the () operator
like functions and methods but it goes beyond just those two…
many other objects in Python are also callable
To see if an object is callable, we can use the built-in function: callable
callable(print) → True
callable('abc'.upper) → True
callable(callable) → True
callable(str.upper) → True
callables always return a value
callable(10) → False

Different Types of Callables
built-in functions--- print, len, callable
built-in methods ------- a_str.upper, a_list.append
user-defined functions created using def or lambda expressions
methods functions bound to an object
classes MyClass(x, y, z)
        → __new__(x, y, z)
        → __init__(self, x, y, z)
        → returns the object (reference)
        → creates the new object
class instances if the class implements __call__ method
generators, coroutines, asynchronous generators

"""
print('------------------------------')
print('is print a callable function: ')
print(callable(print))  # True

# every callable returns a value
print('------------------------------')
result = print('hello')
print('What is the return type of print function ')
print(result)

print('------------------------------')
l = [1, 2, 3]
print('is append a callable function: ')
print(callable(l.append))
result = l.append(4)
print(l)
print('What is the return type of append function on a list')
print(result)

print('------------------------------')
s = 'abc'
print('is upper a callable function: ')
print(callable(s.upper))
result = s.upper()
print('What is the return type of upper function on a list')
print(result)

print('------------------------------')
# classes are also returnable, lets look at inbuilt decimal class
print('is decimal class a callable function: ')
print(callable(decimal.Decimal))
print('What is the return type of decimal class on a value 10.56')
a = decimal.Decimal('10.56')
print(a)
print("What is the return type of a  where a = decimal.Decimal('10.56') ")
print(type(a))
print("is 'a' a callable function: ")
print(callable(a))  # Not callable, instance of a decimal class is not callable


# To make instance of a class callable we need to use dunder call method in your class
# Lets see if instance of a class is callable without dunder call method
print('--------------instance of a class is NOT callable without dunder call method')
class MyClass:
    def __init__(self,x=1):
        print('initializing counter')
        self.counter = x


a = MyClass(100)
print(a.counter)
print('Is instance of a class callable without dunder call method?')
print(callable(a))


print('------------instance of a class is callable with dunder call method')

class MyClass:
    def __init__(self,x=1):
        print('initializing counter')
        self.counter = x

    def __call__(self, x=0):
        print('callable...')
        self.counter += x

b = MyClass(100)
print(b.counter)
print('Is instance of a class callable with dunder call method?')
print(callable(b))

# to call the dunder call method
MyClass.__call__(b,10)
print(b.counter)
print('----------------')
# we can call b method directly as its callable
b()
print(b.counter)
b(50)
print(b.counter)


