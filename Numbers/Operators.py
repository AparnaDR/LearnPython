import math
"""
Operators supported by Integers are
addition +
subtraction -
multiplication *
division /
exponents **

Return type of each operators
int + int → int
int - int → int
int * int → int
int / int → float
but, also 10 / 2 → 5 (float)
obviously 3 / 4 → 0.75 (float)

Two more operators in integer arithmetic

1. long integer division…
example
155/4 = 38 with remainder 3
Fractions

   38 -----> 155 // 4 ---> Floor division
  ___
4|155
  12
  ___
   35
   32
   __
    3 ---> Reminder ---> 155 % 4 (Modulus operator gives the remainder
ALso
155 = 4 * 38 + 3 same as above

and they always satisfy:
n = d * (n // d) + (n % d)
155 = 4 *(155 // 4) + (155 % 4)
155 = = 4 * 38 + 3

What is floor division exactly?
First define the floor of a (real) number
is the largest (in the standard The floor of a real number a number order) integer <= a
floor(3.14) → 3 -- Do a fraction to understand this
floor(1.9999) → 1
But watch out for negative numbers!
floor(-3.1) -4

a // b = floor(a / b)

"""

# Return type of each operators
# int + int → int
print(type(1+1))

# int - int → int
print(type(1-1))

# int * int → int
print(type(1*1))

# int ** int → int
print(type(2**2))

# int / int → float
print(type(5/3))
print(type(10/2))
print(10/2)

# floor

print(math.floor(3.2))
print(math.floor(3.9999999999999))
print(math.floor(-3.2))
print(math.floor(-3.000000000001))
print(math.floor(-3.0000000000000001)) # limited precision

print('-----------+ve------------------')
a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))

print('-----------negative------------------')
a = -33
b = 16 # -3
print(a/b)  # -2.0625
print(a//b)  # largest integer less than -2(a/b) that is  -3
print(math.floor(a/b))  # -3
print(math.trunc(a/b))  # -2

# formula verification for all scenarios
print('-----------formula verification------------')
print('n = d * (n // d) + (n % d)')
print('------pos/pos-------------')
a = 13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + (a%b))

print('------neg/pos-------------')
a = -13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + (a%b))

print('------pos/neg-------------')
a = 13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + (a%b))

print('------neg/neg-------------')
a = -13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + (a%b))
