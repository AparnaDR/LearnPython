# positional and keyword arguments


def my_func(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))


my_func(1, 2, 3)  # position arguments


# if we dont pass any argument we will get error, so we can specify default parameter
# if be provide default for b then all the next parameters should have default parameter

def my_func(a, b=100, c=200):
    print("a={0}, b={1}, c={2}".format(a, b, c))


my_func(1)  # default values will be taken if we dont pass any data
my_func(10, 20, 30)  # if we pass any arguments then default values will not be called

# keyword arguments
my_func(c=3, b=2, a=1)  # not positional we can mix as long as we are providing the variable name
my_func(11, c=2, b=1)
my_func(11, b=1)  # b will take default values

# ---unpacking tuples.---
# Representation of tuples
# Parenthesis is not getting considered for tuple, but comma
a = (1, 2, 3)
print(type(a))

a = 1, 2, 3
print(type(a))

# tuple with single element
a = (1)  # int class
print(type(a))

a = (1,)  # tuple class
print(type(a))

a = 1,  # tuple class
print(type(a))

# if we need empty tuple then we need parentheses
a = ()
print(type(a))

# unpacking list
a, b, c = [1, 'a', 3.14]
print("a, b, c values : {0}, {1}, {2}".format(a, b, c))

(a, b, c) = [1, 'a', 3.14]
print("a, b, c values : {0}, {1}, {2}".format(a, b, c))

# unpacking tuple
(a, b, c) = (1, 'ab', 10.14)
print("a, b, c values : {0}, {1}, {2}".format(a, b, c))

# unpacking variables
a, b, c, c, d = 1, 'ab', 10.14, {1, 2}, ['a', 'b']
print(a, b, c, d)

# swap two numbers using unpacking

a, b = 10, 20
print(a, b)

b, a = a, b
print(a, b)

# unpacking string
for a in 'APARNA':
    print(a)

a, b, c = 'XYS'
print("a, b, c values : {0}, {1}, {2}".format(a, b, c))

# unpacking sets , we can unpack but they dont return in same order, there is no guarantee of the order

s = {'a', 'b', 'c'}
print(s)

for e in s:
    print(e)

a, b, c = s
print("a, b, c values : {0}, {1}, {2}".format(a, b, c))

# unpacking maps
# order is not guaranteed


d = {'a': 1, 'b': 2, 'c': 3}

# below will only print the keys, we can unpack only keys

for e in d:
    print(e)

a, b, c = d
print("a, b, c values : {0}, {1}, {2}".format(a, b, c))

# unpacking values in maps
for e in d.values():
    print(e)

a, b, c = d.values()
print("a, b, c values : {0}, {1}, {2}".format(a, b, c))

# unpacking keys and values in maps, return type of each map is a tuple
# order is not guaranteed

for e in d.items():
    print(e)

for e in d.items():
    a, b = e
    print('key = {0} , value = {1} '.format(a, b))

for a, b in d.items():
    print('key = {0} , value = {1} '.format(a, b))