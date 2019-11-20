import operator
from functools import reduce
print(dir(operator))

print(operator.add(1, 2))
print(operator.mul(2, 3))
print(operator.truediv(3, 2))
print(operator.floordiv(13, 2))  # 13//2

print(reduce(lambda x, y: x*y, [1,2,3,4]))

print(reduce(operator.mul,[1, 2,3,4]))
print(operator.lt(10, 2))
print(operator.is_('abc', 'def'))
print(operator.is_('abc', 'abc'))
print(operator.truth([]))
print(operator.truth([1,2]))

# getters and setters
my_list = [1, 2, 3, 4]
print(my_list[1])

res = operator.getitem(my_list, 1)
print(res)

my_list[1] = 100
print(my_list)
del my_list[3]
print(my_list)
# using operator

my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
print(my_list)

operator.delitem(my_list, 3)
print(my_list)

# itemgetter
f = operator.itemgetter(2)
print(type(f)) # its a callable
my_list = [1, 2, 3, 4]
print(f(my_list)) # 4rd item will return

s = 'python'
print(f(s))  # will give 't'


f = operator.itemgetter(2, 3)
print(type(f)) # its a callable
my_list = [1, 2, 3, 4]
print(f(my_list)) # 3rd  and 4th item will return in a tuple format
print(f('python'))  # retruns t and h


# attribute getter

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method is running')

    def test1(self, d, e, *, f):
        print(self.a, self.b, self.c, d, e, f)

obj = MyClass()

print(obj)  # will return the memory location
print(obj.a, obj.b, obj.c) # normal way of calling atribute
print(obj.test)  # will return the memory location
print(obj.test())  # will call the method

# now lets use the attribute getter method

prop_a = operator.attrgetter('a') # will return a callable fun
print(prop_a)
print(prop_a(obj)) # we need to call them as a fun for the obj type

# the above is useful when the value of a comes from another variable
my_var = 'b'
#print(obj.my_var)  # this will give error, instead you can put the the b value to my_var using a attrgetter instead
# of directly assigning it

prop_b = operator.attrgetter('b')
# now my_var is a callable
print(prop_b(obj))

# in future if you decide to change the value of my_var and call it it still will display old value
my_var = 'c'
print(prop_b(obj))  #  will still print b's value that is 20

# attgetter can take more than one arguments

print('-----------------------')
a, b, test = operator.attrgetter('a', 'b', 'test')(obj)
print(a)
print(b)
print(test)
test()  # test method in my class has a print method and returns nothing to print here

print('-----------------------')

# using lambda

f = lambda x: x.a
print(f(obj))

f = lambda x: (x[2], x[3])

x = [1, 2, 3, 4]
print(f(x))

print('-----------------------')

#sorting the real num of the list of complex numbers

a = 5+ 10j
print(a.real)  # 5.0
print(a.imag)  # 10.j

l = [5-10j, 3+3j, 2-100j]

print(sorted(l , key=lambda x: x.real))

# using attgetter
print('-----------------------')

print(sorted(l, key=operator.attrgetter('real')))

# sort based on first item of the tuple
l = [(2, 3, 4), (1, 4, 5), (4,), (6, 100)]
print(sorted(l, key = lambda x : x[0]))

# using attgett
print(sorted(l, key= operator.itemgetter(0)))

# method called
# lets call the method test from myclass

f = operator.attrgetter('test')  # here we are calling method using attgetter
f(obj)()

# using methodcaller fun

f = operator.methodcaller('test')  # here we are calling method using method called
f(obj)


# incase if the method has a parameter positional and keyword parameter
# calling normally using obj name
obj.test1(100, 200, f= 500) # 10, 20, 30, 100

# using method caller
operator.methodcaller('test1', 100, 200, f= 500)(obj)

# calling test1 method using attcaller
f = operator.attrgetter('test1')
f(obj)(100, 200,f=500)




