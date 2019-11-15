# Lambda expressions are simply another way to create functions
# it can be assigned to a variable
# passed as an argument to another function
# The "body" of a lambda is limited to a single expression


# regular function using def
def sq(x):
    return x ** 2


print(type(sq))

f = sq
print(id(f), id(sq))  # both are pointing to same memory location
print(f(2))
print(sq(2))
print(f)  # still points to sq

# same using lambda
print('---lambda-------')
f1 = lambda x: x ** 2

print(f1)
print(f1(2)) # f1 is callable

print('---lambda with default values-------')
g =lambda x, y=10: x+y

print(g(1))
print(g(1,2))

print('---lambda with positional and keyword arguemnts-------')
f2 = lambda  x, *args, y, **kwargs: (x + y, *args, kwargs)

print(f2(10, 'a', 'b', a1=10, b2=20, y=10))

print('---passing lambdas as functions-------')

def apply_fun(x, fn):
    return fn(x)

print(apply_fun(3, sq))

print(apply_fun(5, lambda x: x**3))

print('---passing lambdas as functions which has starred postional and keyword arguments-------')
def apply_func_star(fn, *args, **kwargs):
    return fn(*args, **kwargs)


print('------- passing existing normal function--------')
print(apply_func_star(sq, 4))

print('------- passing lambda expression with only 1 positional arg--------')
print(apply_func_star(lambda x: x**2, 6))

print('------- passing lambda expression with 2 positional arg--------')
print(apply_func_star(lambda x, y: x+y, 2, 3))

print('------- passing lambda expression with 1 positional arg and 1 keyword arg--------')
print(apply_func_star(lambda x, *, y: x+y, 1, y=100))

print('------- passing lambda expression with many positional arg to calculate sum of those arguments-------')
print(apply_func_star(lambda *args: sum(args),1, 2, 3, 4, 5))

print('------- passing inbuilt function to calcualte sum-------')
print(apply_func_star(sum,(1, 2, 3, 4, 5)))



