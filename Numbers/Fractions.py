# Rational numbers are fractions of  intger class
# 22/3 , -22/7 ,1/2
# by default if you dont specify denominator it takes 1

from fractions import Fraction

# print(help(Fraction))

# Constructors
print('----default constructor-----------')
print(Fraction(2)) # by default if you dont specify denominator it takes 1
print(Fraction(2, 1))
a = Fraction(4, 2)
print(a)
print(a.denominator, a.numerator)  # 4/2 will be reduced to 1/2 by python

print('--float const---------')
print(Fraction(0.125))

print('--division const---------')
print(Fraction('22/7'))

x = Fraction(2, 3)
y = Fraction(3, 4)

print(x+y)
print(x/y)

print(Fraction(1/-4))