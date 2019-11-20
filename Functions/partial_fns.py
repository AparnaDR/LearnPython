from functools import partial
# -----------------------

def my_func(a, b, c):
    print(a, b, c)

def f(x, y):  # reducing no of arguments on main func
    return my_func(10, x, y)

f(20, 30)

f = lambda x, y: my_func(10, x, y)
f(100, 200)

f =  partial(my_func,10 )
f(20, 30)

f =  partial(my_func,10, 20)
f(30)
# -----------------------

# with more complex arguments
# -----------------------

def my_func(a, b, *args, k1, k2, **kwargs):
    print((a, b, args, k1, k2, kwargs))

my_func(10,20, 100, 200, 300, k1 = 'kw1', k2 = 'kw2', k3 = 'ex1', k4= 2000)


# reduce no of arguments by creating another fun
def f(x, *vars, kw, **kwvars):
    return my_func(10, x, *vars, k1 = 'a', k2=kw, **kwvars)

f(20, 30, 40, 50, kw = 1, kw1= 22, kw2 = 22)

# reduce using partial
f = partial(my_func, 10, k1='a')
f(20, 100,200, k2 = 'b', k3 = 4000)

# -----------------------

def pow(base, exponent):
    return base ** exponent

sq = partial(pow, exponent=2)
print(sq(5)) # passing only base

cube = partial(pow, exponent=3)
print(cube(5))

# we can change the exponent value while calling the fun
print(cube(5, exponent=5)) # 5**5

#
a = 2
sq = partial(pow, exponent=a)
print(sq(5)) # 5 **2

a =3
print(sq(5)) # still it takes 5 **2 as its not calling the function with changed value

# -----------------------

def my_func(a, b):
    print(a, b)

a = [1, 2]
f = partial(my_func, a)
f(100)  # passing b value here
# output = [1, 2] 100

a.append(3)  # not changing value only modifying
print(a)
f(100)  # passing b value here
# now output is -- [1, 2, 3] 100

# -----------------------

# sort a list of co ordinates based on the origin distance
origin = (0,0)
l = [(1,1), (0, 2), (-3, 2), (0,0), (10, 10)]
dist2 = lambda a, b: (a[0] - b[0]) **2+ (a[1] - b[1])**2  # here a take (1,1) , b takes origin

print(dist2((1, 1), origin))

f = partial(dist2, origin) # b values
print(f((1, 1)))  # a value

print(sorted(l , key = f))

# another way to achive using lambda instead of partial

f = lambda x : dist2(origin, x)
print(sorted(l, key=f))


