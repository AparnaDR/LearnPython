# Everything is an object in python

"""
a = 10
print(type(a))  # 'a' is type class

print(help(int))

c = int()  # normal way of calling any class variable name =  class_name()
print(c)  # by default value is 0 . See help(int) class

# by default base 10 is used, incase you need it in binary

c = int('101', base=2)
print(c)

"""


# functions are objects too


def square(a):  # defining function
    return a ** 2


print(square(2))  # calling function

print(type(square))  # square is of function type

#  we can assign variable to a function

f = square

print(id(f), id(square))  # both are pointing to same memory address, shared references

print(f is square)  # True

# calling square function
print(square(3))

# calling through variable
print(f(4))


# functions calling function

def cube(a):
    return a ** 3


def function_type(id_num):
    if id_num == 1:
        return square
    else:
        return cube


f1 = function_type(1)
print(f1 is square)

f1 = function_type(2)  # f1 is just assigned to the cube memory location, on printing f1 you will see only mem add
print(f1 is cube)
print(f1(2))  # you can call the function using the variable now f1 is pointed to cube so 8 will be printed

# to call it directly

print(function_type(2)(2))  # first argument to figure which function to execute and second is the function argument


# we can also pass function as an argument in another function


def execute_func(fn, n):
    return fn(n)


print(execute_func(cube, 3))
print(execute_func(square, 3))
