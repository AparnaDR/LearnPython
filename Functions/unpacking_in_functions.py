# starred expns as function parameters
# *args us used to scoop up all remaining positional arguments
# **kwargs us used to scoop up all remaining keyword arguments
# args and kwargs are only a convention, not mandatory to be followed. * and ** represents the exps
# two ways of passing arguments
# 1. positional arguments - 1st argument goes to 1st parameter in a function
# 2. keyword arguments - based on the keyword mapped while calling a function that is assigned to the variable within
# the function
# *args returns tuples
# **kwargs returns dictionaries
# No parameters can come after **kwargs

print('-----starred expns as function parameters--------- ')


def func1(a, b, *args):  # *args returns tuples
    print(a)
    print(b)
    print(args)


func1(10, 20)  # args will have empty tuple
func1(10, 20, 1, 2, 3)  # *args will have 1,2,3 in a single tuple

print('-----------calculate average-----------')


# calculate avg
def avg(a, *args):  # here you are forcing the user to enter one parameter for sure
    count = len(args) + 1
    total = sum(args) + a
    #  #return count and total/count  # we can use this also,
    if count == 0:
        return 0
    else:
        return total / count


print(avg(2, 2, 4, 4))

print('-----------unpacking list and passing it into a function as argument-----------')


def func2(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)


l = [10, 20, 30, 40, 50, 60]
func2(*l)

#  **kwargs
# We can send any no od keyword arguments

print('------------passing n number of keyword arguments only----------')


def func(**kwargs):
    print(kwargs)


func(a=1, b=2, c=3)  # We need to pass keyword arguments only . ANd it returns dictionaries

print('------------passing n number of keyword and positional arguments ----------')


def funca(*args, **kwargs):
    print(args)
    print(kwargs)


funca('a', -98, 0.234, a=1, b=2, c=3, d=4)  # We need to pass positional arguments and then only keyword arguments
# positional arguments returns tuple and keyword arguments returns dictionaries


print('------------passing keyword and positional arguments ----------')


def func(a, b, *, d, **kwargs):  # * indicates end of positional parameters
    print(a)
    print(b)
    print(d)
    print(kwargs)


func(1, 2, d=200, c=100, d1=800)


def calc_hi_lo_avg(*args, log_to_console=False):
    hi = max(args) if len(args) > 0 else 0
    lo = min(args) if len(args) > 0 else 0
    avg1 = (hi + lo) / 2
    if log_to_console:
        print("high = {0} , low = {1}, avg = {2}".format(hi, lo, avg1))
    return avg


avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=True)


def func(*, a=100, b=200, c):
    print(a, b, c)
# star in the beginning means no positional arguments. a and b has default values. c needs to be passed with some value
