# docstrings and annotations
# similar to help functions we can write help for our classes and functions

# help(int)
# help(print)


# first line inside the function is considered as  document
def my_func(a, b=1):
    """returns a * b

    input:

    output:
    """
    return a * b


print(help(my_func))
print(my_func.__doc__)


# annotations


def my_funca(a: 'annotation for a',
             b: 'annotation for b' = 1) -> 'annotation for saying the return type':
    """docstring for my_funca"""

    return a * b


print(my_funca(11, 12))
help(my_funca)
my_func.__annotations__
my_funca.__doc__

x = 3
y = 5


# here annotations will get processed
def my_func1(a: 'input any character') -> 'character a repeated ' + str(max(x, y)) + ' times':
    return a * max(x, y)


print(my_func1('a'))
# annotations max 5 is getting calculated and printed in dunder annotations
print(my_func1.__annotations__)
print(my_func1.__doc__)


def my_func2(a: str,
             b: 'int > 0' = 1,  # b defaults to 1 if not provided
             *args: 'some positional args',
             k1: 'keyword-only arg 1',
             k2: 'keyword-only arg 2' = 100,
             **kwargs: 'some extra keyword-only args') -> 'sometheing':
    print(a, b, args, k1, k2, kwargs)


print('----------help ----------------')
help(my_func2)
my_func2('www', 22, 1, 2, 3, 4, k1 =100, k2= 200, ex = 11, ex2 = 22)
