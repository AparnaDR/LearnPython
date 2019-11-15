# functions with parameters

import math
from math import sqrt



def greet_user(fname, lname):  # parameters

    print(f"Hi {fname} {lname}")
    print("Welcome aboard!!")


greet_user("Aparna", "Sandesh")  # positional arguments, 1st argument goes to 1 st parameter and so on
greet_user(lname = "Raghavendra",fname = "Archana") # keyword argument: here position doesnt matter, usually used
# when arguments are of number type within same function call if you are giving both positional arguments and
# keyword argument, positional argument should be first, else you will get error
print("end of program")

# Function with return type


def square(number):
    return number * number


print(square(2))
# -------------------
# in above example if we dont return and directly print in the definition then the print below will return none,
# as the above def does not return anything back


def square(number):
    print(number * number) # by default return none, like null in java


print(square(2))



# built in functions

s = [1,2,3]
len(s)

# need to import math module
sqrt(4)
math.pi
math.exp(1)