from inspect import isfunction, ismethod, isroutine, getsource, getmodule, getcomments, signature
import math

# dummy code
i = 100


# TODO: Fix this function
# currently not working
def my_func(a: "mandatory positional",
            b: "optional positional" = 1,
            c=2,
            *args: "add extra positional here",
            kw1: "mandatory keyword",
            kw2: "optional keyword" = 100,
            kw3=200,
            **kwargs: "provide extra keyword args here") -> "no return":
    """ This function does nothing but has annotation and documentation"""
    i = 10
    j = 20
    a = i+j
    return a

print(my_func.__doc__)
print(my_func.__annotations__)
# we can add description for our function and add it to our attribute and when we call the dunder function it should
# return that

print('----------- adding short dec attribute to your function---------')
my_func.short_description = "func that does nothing"
print(my_func.short_description)
# dir will show all atrtributes available for my_func
print(dir(my_func))  # we will see that short_description is added to the directory

# lets see some attributes
print('--- name attribute----')
print(my_func.__name__)


def func_call(f):
    print(f.__name__)


func_call(my_func)

print('--- default attribute----')
print(my_func.__defaults__)
print(my_func.__kwdefaults__)

print('--- code directory----')
#  code is itself an object and it has its own directory
print(dir(my_func.__code__))

print('--- code co_name----')
print(my_func.__code__.co_name)

print('--- code co_varnames----')
print(my_func.__code__.co_varnames)

print('--- code co_argcount----')
print(my_func.__code__.co_argcount)  # only positional arguments


# inspect
a = 10
print('-----------------------')
print(isfunction(a))
print(ismethod(a))
print(isroutine(a))

print('-----------------------')
print(isfunction(my_func))
print(ismethod(my_func))  # methods are within a class, need to call using the instance variable of the class
print(isroutine(my_func))

class MyClass:
    def f(self):
        pass
print('-----------------------')
print(isfunction(MyClass.f)) # if we call directly using the class name it is a function
print(isroutine(MyClass.f))

print('-----------------------')
obj = MyClass()
print(isfunction(obj.f)) # if you call using an object name then its not a function but its a method
print(ismethod(obj.f))
print(isroutine(obj.f))

print('-------source code----------------')
# get source code
print(getsource(my_func))

print('-------module ----------------')
# get module
print(getmodule(my_func))
print(getmodule(print))
print(getmodule(math.sin))

# to find all the comments. this is not documentation, fetches only comments
print(getcomments(my_func))

# to get signature
print(signature(my_func))
print(dir(signature(my_func)))
print(my_func.__annotations__)
print(signature(my_func).return_annotation)

sig = signature(my_func)
print(sig.parameters)

# here in below code we are printing every parameters name, default value, annotation, kind etc.
print('-----signature parameters--------')
for param in sig.parameters.values():
    print('Name: ', param.name)
    print('Default: ', param.default)
    print('Annotation: ', param.annotation)
    print('Kind: ', param.kind)
    print('-------------------------------')


# Kind
"""
POSITIONAL_OR_KEYWORD
VAR_POSITIONAL -- *args
KEYWORD_ONLY
VAR_KEYWORD --- **kwargs
"""

print(help(divmod)) # the help shows this function takes 2 parameters and then a /. it means this function
# only accepts positional arguments and it wont accept key word.

print(divmod(4, 3))  # works fine
# print(divmod(x=4, y=3)) # error -- TypeError: divmod() takes no keyword arguments

print('----- signature of divmod inbuilt function -------')
# we can check using inspects signature parameters as above
# divmod has two parameters x and y which are positional only
# only python can have such code, our functions cannot mandate positional only
for param in signature(divmod).parameters.values():
    print('Name: ', param.name)
    print('Default: ', param.default)
    print('Annotation: ', param.annotation)
    print('Kind: ', param.kind)
    print('-------------------------------')






